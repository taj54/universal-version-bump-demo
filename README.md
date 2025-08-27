# Universal Version Bump Demo

This repository serves as a demonstration for the `universal-version-bump` GitHub Action. It showcases how the action can automatically update version numbers across various programming languages and package manager configurations within a monorepo or a project with diverse language components.

## Demo Structure

Each subdirectory within this repository represents a different programming language or package management ecosystem, demonstrating how the `universal-version-bump` action can target and update version numbers in their respective configuration files:

*   `node-demo/`: Demonstrates version bumping in a Node.js `package.json` file.
*   `php-composer-demo/`: Demonstrates version bumping in a PHP `composer.json` file.
*   `php-config-demo/`: Demonstrates version bumping in a custom PHP `config.php` file.
*   `php-version-php-demo/`: Demonstrates version bumping in a PHP class constant defined in `Version.php`.
*   `python-setup-demo/`: Demonstrates version bumping in a Python `setup.py` file.
*   `python-toml-demo/`: Demonstrates version bumping in a Python `pyproject.toml` file.
*   `rust-demo/`: Demonstrates version bumping in a Rust `Cargo.toml` file.

## How to Use the Demo

The version bumping functionality is handled by a GitHub Actions workflow located at `.github/workflows/universal-version-bump-node.yml`. To observe the action in practice:

1.  **Fork this repository** to your own GitHub account.
2.  Navigate to the **"Actions"** tab in your forked repository.
3.  Select the **"Version Bump"** workflow from the left sidebar.
4.  Click on the **"Run workflow"** dropdown button.
5.  You will be presented with two inputs:
    *   **`release_type`**: Choose the type of version bump (e.g., `patch`, `minor`, `major`).
    *   **`target_path`**: Select the specific demo directory (e.g., `node-demo`, `python-toml-demo`) where you want the version to be bumped.
6.  Click the **"Run workflow"** button to trigger the action.

After the workflow completes, a new commit will be pushed to your repository with the updated version number in the specified `target_path`'s configuration file. You can inspect the commit history to see the changes made by the action.

This demo provides a clear example of how to integrate `universal-version-bump` into your CI/CD pipeline to automate version management across diverse projects.
