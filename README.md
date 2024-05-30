# Analyze Home Assistant database

<a target="_blank" href="https://colab.research.google.com/github/tonka3000/analyze-ha-db/blob/main/check_ha_db.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

The notebook can be used analyze a copy of the Home Assistant sqlite database to ...

- Get the states with the most updates
- Get the events counts

This data can be used to exclude certain entities in the [Home Assistant recorder](https://www.home-assistant.io/integrations/recorder/#configure-filter) to reduce the amount of data which is stored in the database to keep it efficient.

More information about the process can be found in the excellent [post from Denilson Sá Maia](https://community.home-assistant.io/t/how-to-keep-your-recorder-database-size-under-control/295795).
Most of the SQL queries from the post are used in this notebook.

Thank you [Denilson Sá Maia](https://github.com/denilsonsa) for the great work 🙏

## Setup

You need a working Jupyter notebook environment with pandas and plotly installed.

### Google Colab

The easiest way to get such an environment is [Google Colab](https://colab.research.google.com).

Press the `Open in Colab` button at the top of this document and click on `Runtime` (Menu Bar) and on `Run All`.

If the `get_from_gdrive_backup` option in the notebook is `True` (which is the default) you well see a popup which will ask for permission to access your Google Drive.

:warning: Be aware that your data is stored/processed on Google Servers!

### Local Jupyter

You can use a local installed Jupyter as well. This can be installed via conda or pip.

As frontend you can use [Jupyter](https://jupyter.org) or [VSCode](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).

Just make a local copy of the notebook and open it in your frontend of choice.

## Database Copy

Grab a copy of the Home Assistant sqlite database file `home-assistant_v2.db` and put it next to this notebook.
It is also possible to change the path to the db filename in the notebook.

There a various ways to get the database file

- Extract it from you backup tar-file (e.g. Google Drive or Local Server)
- Copy it via `scp`
- Use Google Colab with the same account as your backups are stored

### Secure Backup

You need to use `extract_from_secure_backup.py` if your backup is protected by a password.
On Windows, you also need Docker installed and running to be able to extract the database from the backup file.

`python extract_from_secure_backup.py "<Path to your backup file>"`

The backup file should be stored in the `data` directory next to this README file you are actually reading.

After running successfully, you will be prompted to enter your password.
Once entered, the database file will be placed in the root directory of this repository.

## License

The notebook itself is licensed under MIT license.
