import click
from bw2preagg.balancing_presamples import generate_balancing_presamples
import json

@click.command()
@click.option('--project_name', default='default', help='Brightway2 project name', type=str)
@click.option('--database_name', help='Database name', type=str)
@click.option('--result_dir', help='Base directory path for results', type=str)
@click.option('--iterations', help='Number of iterations in sample batch', type=int)
@click.option('--samples_batch', help='Sequential integer id for sample batch', type=int)
@click.option('--overwrite_ps', help='Overwrite presamples package if exists', default=True, type=bool)
@click.option('--balance_water', help='Balance water exchanges', default=True, type=bool)
@click.option('--balance_land', help='Balance land transformation exchanges', default=True, type=bool)
@click.option('--ecoinvent_version', help='ecoinvent release number, used by water exchange balancer', default='3.6', type=str)
@click.option('--expect_base_presamples', help='Raise error if base presamples do not exist', default=True, type=bool)
@click.option('--land_balancing_patter_fp', help='File with land transformation patters', default=None, type=str)
def generate_balancing_presamples_CLI(
        project_name, database_name, result_dir, iterations, samples_batch,
        overwrite_ps=True, balance_water=True, balance_land=True,
        ecoinvent_version="3.6", expect_base_presamples=True, land_balancing_patter_fp=None):
    """CLI-friendly access to bw2preagg.generate_balancing_presamples, to generate balancing presamples for a given db"""
    if land_balancing_patter_fp:
        with open(land_balancing_patter_fp, 'r') as f:
            land_balancing_patters = json.load(f)
        generate_balancing_presamples(
            project_name=project_name,
            database_name=database_name,
            result_dir=result_dir,
            iterations=iterations,
            samples_batch=samples_batch,
            overwrite_ps=overwrite_ps,
            balance_water=balance_water,
            balance_land=balance_land,
            ecoinvent_version=ecoinvent_version,
            land_from_patterns=land_balancing_patters['land_from'],
            land_to_patterns=land_balancing_patters['land_to'],
            expect_base_presamples=expect_base_presamples
        )
    else:
        generate_balancing_presamples(
            project_name=project_name,
            database_name=database_name,
            result_dir=result_dir,
            iterations=iterations,
            samples_batch=samples_batch,
            overwrite_ps=overwrite_ps,
            balance_water=balance_water,
            balance_land=balance_land,
            ecoinvent_version=ecoinvent_version,
            expect_base_presamples=expect_base_presamples
        )


if __name__ == '__main__':
    __spec__ = None
    generate_balancing_presamples_CLI()