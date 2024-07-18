# Playwright Demo Project Setup

This project sets up a Python virtual environment and installs necessary dependencies, including Playwright, to run a demo test using `pytest`.

## Prerequisites

Make sure you have the following installed on your system:

- **Operating System**: Debian 11, Debian 12, Ubuntu 20.04, Ubuntu 22.04, or Ubuntu 24.04
- **Architecture**: x86-64 or arm64
- **Python**: Python 3.8+
- `sudo` privileges
- Internet connection for downloading packages

## Setup Instructions

1. **Clone the repository** (if applicable):

2. **Run the setup script**:
Run `source install.sh`. The setup script will replace the existing `playwright_venv` folder with a fresh one, update your system packages, and install the necessary Python packages and Playwright browsers.

3. **Run the demo test**:
Once the setup is complete, you can run the demo test using `pytest test_demo.py`.

## Explanation of `install.sh`

The `install.sh` script performs the following steps:
1. Prompts the user to confirm if they want to replace the existing `playwright_venv` folder.
2. Deactivates any active Python virtual environment.
3. Removes the existing `playwright_venv` folder if it exists.
4. Updates system packages.
5. Installs necessary packages: `python3-venv`, `figlet`, `jp2a`, and `python3-pip`.
6. Creates and activates a new Python virtual environment (`playwright_venv`).
7. Upgrades `pip` to the latest version.
8. Installs Python packages listed in `requirements.txt`.
9. Installs Playwright browsers.
10. Displays a success message using `figlet`.

### Notes

- The script uses `sudo` for package installation and removing directories. Ensure you have the necessary privileges to run `sudo` commands.
- The `requirements.txt` file should be in the same directory as `install.sh` and list all the required Python packages for your project.
- In case you need to activate a virtual env in Python run in the project folder `source playwright_venv/bin/activate`. To deactivate it run `deactivate`.

## Troubleshooting

- If you encounter network issues during package installation, ensure you have a stable internet connection.
- If the script fails at any step, check the error message, resolve the issue, and rerun the script.
- Make sure the `requirements.txt` file exists and is correctly formatted.

## Useful Links

- [GitHub Cloning Guide](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
- [Playwright Python Documentation](https://playwright.dev/python/docs/intro)


## License

This project is licensed under the MIT License.
For more information, please visit [MIT License on GitHub](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt).
