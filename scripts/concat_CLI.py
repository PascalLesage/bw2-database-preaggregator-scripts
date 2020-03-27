import click
import json
from bw2preagg.concat_batches import concat_lcia_samples_arrays_from_method_tuple, concat_samples_arrays_in_result_type_dir


@click.command()
@click.option('--result_dir', help='Base directory path for precalculated samples', type=str)
@click.option('--concat_result_type', help='LCI or LCIA', type=str, default='LCI')
@click.option('--method_list_file_path', help='Filepath to list of methods', default=None, type=str)
@click.option('--method_idx', help='Index of selected method in list', type=int, default=0)
@click.option('--concat_totals_or_per_exchanges', help='Concatenate arrays of total scores or scores per elementary flow', type=str, default="totals")
@click.option('--sim_name', help='Name to give the directory in which results will be saved', type=str, default=None)
@click.option('--dest', help='Path to location where concatenated array directory will be saved', type=str, default=None)
@click.option('--fail_if_samples_batches_different', help='If False, will raise ValueError if arrays available in samples_batch folders are not the same', type=bool, default=False)
@click.option('--ignore_missing_concat', help='If True, run even if not all LCI arrays present', type=bool, default=False)
@click.option('--project_name', help='Name of the project', type=str, default=None)


def concat_CLI(
        result_dir, concat_result_type, method_list_file_path, method_idx,
        concat_totals_or_per_exchanges, sim_name, dest,
        fail_if_samples_batches_different, ignore_missing_concat, project_name):
    """CLI-friendly access to bw2preagg.lcia.save_all_lcia_score_arrays"""

    if concat_result_type == "LCIA":
        if not all([method_list_file_path, method_idx]):
            raise ValueError("You need to pass method_list_file_path and method_idx to concatenate LCIA arrays")
        with open(method_list_file_path, 'r') as f:
            method_dict = json.load(f)
        method = tuple(method_dict[str(method_idx)])
        concat_lcia_samples_arrays_from_method_tuple(
            result_dir=result_dir,
            method=method,
            sb_id_list=None,
            totals_or_per_exchanges=concat_totals_or_per_exchanges,
            project_name=project_name,
            sim_name=sim_name,
            dest=dest,
            fail_if_samples_batches_different=fail_if_samples_batches_different,
            ignore_missing=ignore_missing_concat
        )
    else:
        concat_samples_arrays_in_result_type_dir(
            result_dir=result_dir,
            sb_id_list=None,
            result_type_dirname="LCI",
            totals_or_per_exchanges=None,
            sim_name=sim_name,
            dest=dest,
            fail_if_samples_batches_different=fail_if_samples_batches_different,
            ignore_missing=ignore_missing_concat
        )


if __name__=='__main__':
    __spec__ = None
    concat_CLI()