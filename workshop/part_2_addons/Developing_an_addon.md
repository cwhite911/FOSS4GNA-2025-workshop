[contributing]: https://github.com/OSGeo/grass-addons/blob/grass8/CONTRIBUTING.md
[cookiecutter]: https://cookiecutter.readthedocs.io/en/stable/
[cookiecutter_install]: https://cookiecutter.readthedocs.io/en/stable/installation.html#install-cookiecutter

# Step-by-Step: How to Contribute an Addon

**_Corey White and Caitlin Haedrich_**

## 1. Fork GRASS addons

We can follow the contributing documentation from the [grass-addons][contributing]
GitHub repository.

## 2. Create a new addon using Cookiecutter

[Cookiecutter][cookiecutter] is set up to help generate the required boiler
plate structure of an addon.

> Cookiecutter is already install in this codespace, but you will need to
install it on your own machine using the following documentation for local
use ([cookiecutter install docs][cookiecutter_install]).

```bash
# Use for the current stable release
# cookiecutter gh:OSGeo/grass-addon-cookiecutter

cookiecutter https://github.com/cwhite911/grass-addon-cookiecutter --checkout grass-tools
```

## 3. Implement the addon functionality

1. Write the core functionality of your addon in the main script file
   (e.g., `r.myaddon.py`).
2. Use GRASS libraries and tools to interact with GRASS data and perform
   operations.
3. Follow best practices for coding style and documentation.
4. Implement error handling and input validation.
5. Write unit tests to ensure the addon works as expected.
6. Write documentation for the addon, including usage instructions and examples.

## 4. Open a pull request to contribute the addon

- Naming conventions
  - Follow GRASS naming conventions for addons.
  - Use a prefix that indicates the type of data the addon works with
    (e.g., `r.` for raster, `v.` for vector).
- Documentation
  - Provide clear and concise documentation for the addon.
  - Include usage examples and explanations of options and flags.
- Testing
  - Ensure that the addon has unit tests and passes all tests.
- Code quality
  - Follow coding style guidelines and best practices.
  - Use pre-commit hooks to check code quality before submitting.
- Be kind and respectful in your communication with reviewers and maintainers.

### PR checklist

- [ ] The addon follows GRASS naming conventions.
- [ ] The addon includes clear and concise documentation.
- [ ] The addon has unit tests and passes all tests.
- [ ] The code follows coding style guidelines and best practices.
- [ ] Pre-commit hooks have been used to check code quality.
