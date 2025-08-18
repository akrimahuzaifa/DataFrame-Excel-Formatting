# Adding a Git Submodule to Your Repository

This guide explains how to add another GitHub repository as a **submodule** to your project. Submodules allow you to include and track a separate repository within your main repository.

## Why Use Submodules?

- Share code between multiple projects.
- Keep dependencies tracked at specific commits.
- Maintain a modular codebase.

---

## Step-by-Step Instructions

### 1. Navigate to Your Project Directory

Open your terminal and go to your main repository’s folder:

```bash
cd path/to/your/main-repo
```

### 2. Add the Submodule

Use the following command to add a repository as a submodule:

```bash
git submodule add https://github.com/akrimahuzaifa/DataFrame-Excel-Formatting.git DataFrame-Excel-Formatting
```

- The first argument is the URL of the repository you want to add.
- The second argument is the folder name/path where the submodule will be placed.

### 3. Commit the Submodule

After adding the submodule, commit the changes:

```bash
git add .gitmodules DataFrame-Excel-Formatting
git commit -m "Add DataFrame-Excel-Formatting as a submodule"
```

### 4. Cloning or Updating Submodules

If you clone this repository in the future, run the following to initialize and pull submodules:

```bash
git submodule update --init --recursive
```

To update the submodule to the latest commit from its remote repository:

```bash
cd DataFrame-Excel-Formatting
git pull origin main
```

---

## Troubleshooting

- **Do not use `git add <repo-url> .`**  
  This will result in an error:  
  `fatal: pathspec 'https://github.com/akrimahuzaifa/DataFrame-Excel-Formatting.git' did not match any files`
- Always use `git submodule add` for adding repositories as submodules.

## References

- [Git Submodules Documentation](https://git-scm.com/book/en/v2/Git-Tools-Submodules)
- [GitHub Docs: Using Submodules](https://docs.github.com/en/get-started/working-with-submodules)

---

## License

This repository and submodule are distributed under their respective licenses. Please check their individual LICENSE files for more information.
