# aUTOeXTRACT
simple cross-platform (UNIX, Windows) script used to recursively extract an archive and output all archived files

---

## Usage

- Your input should be: a zip file of any of the supported types (listed below) that is located within a directory. Note that this zip file should be the only file in the directory. Please refer to _Test_ in this repo.
- Run the script name `recursive_extract.py`, supply an input argument that is the directory name: `python recursive_extract <target directory>`.Ex: `python recursive_extract Test`.
- Be fully certain you are running the script for the correct target directory, as the script will pick up all archives in that directory.
- All extracted files can be located in _<target dir>/<Extract>_ folder when script finishes.

---

## Supported Archive formats
1) `.zip` files
2) `.tgz` files
3) `.gz` files
