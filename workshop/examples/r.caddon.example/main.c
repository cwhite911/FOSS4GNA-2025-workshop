#include <grass/gis.h>
#include <grass/raster.h>
#include <grass/glocale.h>

int main(int argc, char *argv[])
{
    struct GModule *module;
    struct Option *input, *output;
    struct History history;
    int nrows, ncols, row, col;
    int infd, outfd;
    void *inrast;
    DCELL *outrast;

    G_gisinit(argv[0]);
    module = G_define_module();
    G_add_keyword("example");
    module->description = _("Example raster add-on");

    input = G_define_standard_option(G_OPT_R_INPUT);
    output = G_define_standard_option(G_OPT_R_OUTPUT);

    if (G_parser(argc, argv))
        exit(EXIT_FAILURE);

    infd = Rast_open_old(input->answer, "");
    nrows = Rast_window_rows();
    ncols = Rast_window_cols();
    outfd = Rast_open_new(output->answer, DCELL_TYPE);

    inrast = Rast_allocate_d_buf();
    outrast = Rast_allocate_d_buf();

    for (row = 0; row < nrows; row++) {
        Rast_get_row(infd, inrast, row, DCELL_TYPE);
        for (col = 0; col < ncols; col++) {
            DCELL val = ((DCELL *)inrast)[col];
            outrast[col] = val * 2; // simple multiply
        }
        Rast_put_row(outfd, outrast, DCELL_TYPE);
    }

    Rast_close(infd);
    Rast_close(outfd);
    G_short_history(output->answer, "raster", &history);
    Rast_command_history(&history);
    Rast_write_history(output->answer, &history);

    G_done_msg("Output raster <%s> written", output->answer);
    return EXIT_SUCCESS;
}
