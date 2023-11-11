# Analyze Home Assistant database

The notebook can be used analyze a copy of the Home Assistant sqlite database to ...

- Get the states with the most updates
- Get the events counts

This data can be used to exclude certain entities in the [Home Assistant recorder](https://www.home-assistant.io/integrations/recorder/#configure-filter) to reduce the amount of data which is stored in the database to keep it efficient.

More information about the process can be found in the excellent [post from Denilson Sá Maia](https://community.home-assistant.io/t/how-to-keep-your-recorder-database-size-under-control/295795).
Also most of the SQL queries from the post are used in this notebook.

Thank you [Denilson Sá Maia](https://github.com/denilsonsa) for the great work 🙏

## Setup

### Jupyter Notebook

You need a working Jupyter notebook environment (e.g. via conda or pip).

Required dependencies are

- pandas
- plotly

### Database Copy

Grab a copy of the Home Assistant sqlite database file `home-assistant_v2.db` and put it next to this notebook.
It is also possible to change the path to the db filename in the notebook.

There a various ways to get the database file

- Extract it from you backup tar-file (e.g. Google Drive or Local Server)
- Copy it via `scp`

## License

The notebook itself is licensed under MIT license.
