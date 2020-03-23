""" Initial setup of the brightway2 project.

Creates project, imports databases and generates some useful data.
Should be run first.
"""
import click
from bw2preagg.setup_project import setup_project

@click.command()
@click.option('--project_name', default='default', help='Brightway2 project name', type=str)
@click.option('--database_name', help='Database name', type=str)
@click.option('--result_dir', help='Base directory path for results', type=str)
@click.option('--database_dir', help='Directory with ecoSpold files for importing LCI data', type=str)
@click.option('--overwrite_project', help='First delete project if it exists', type=bool, default=False)
@click.option('--overwrite_database', help='First delete database if it exists', type=bool, default=False)
@click.option('--save_det_lci', help='If True, deterministic LCI arrays are saved in the deterministic subfolder', type=bool, default=True)
@click.option('--force_write_common_files', help='Write series of database-related files to result_dir', type=bool, default=True)
@click.option('--default_bw2setup', help='If True, run bw2setup to include default elementary flows and LCIA methods', type=bool, default=True)
def setup_project_CLI(project_name, database_name, result_dir, database_dir,
                      overwrite_project, overwrite_database, save_det_lci,
                      force_write_common_files, default_bw2setup):
    """ CLI-friendly access to bw2preagg.setup_project to create project and import databases, generate common files"""
    setup_project(project_name, database_name, result_dir, database_dir,
                  overwrite_project, overwrite_database, save_det_lci,
                  force_write_common_files, default_bw2setup)

if __name__ == '__main__':
    __spec__ = None
    setup_project_CLI()
