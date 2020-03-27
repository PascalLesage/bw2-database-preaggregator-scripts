import click
import json
from bw2preagg.lcia import save_all_lcia_score_arrays

@click.command()
@click.option('--result_dir', help='Base directory path for precalculated samples', type=str)
@click.option('--method_list_file_path', help='Filepath to list of methods', type=str)
@click.option('--method_idx', help='Index of selected method in list', type=int, default=0)
@click.option('--result_type', help='probabilistic or deterministic', type=str, default='probabilistic')
@click.option('--samples_batch', help='Integer representing the presample package', type=int, default=None)
@click.option('--dtype', help='dtype of LCIA array', type=str, default="float32")
@click.option('--return_total', help='Save an array of total scores', type=bool, default=True)
@click.option('--return_per_exchange', help='Save an array of characterized elementary flows', type=bool, default=False)
@click.option('--ignore_missing', help='If True, run even if not all LCI arrays present', type=bool, default=False)
@click.option('--project_name', help='Name of the project', type=str, default=None)
def lcia_CLI(result_dir, method_list_file_path, method_idx,
             result_type, samples_batch, dtype, return_total,
             return_per_exchange, ignore_missing, project_name):
    """CLI-friendly access to bw2preagg.lcia.save_all_lcia_score_arrays"""
    with open(method_list_file_path, 'r') as f:
        method_dict = json.load(f)
    method = tuple(method_dict[str(method_idx)])
    save_all_lcia_score_arrays(
        result_dir=result_dir,
        method=method,
        result_type=result_type,
        samples_batch=samples_batch,
        dtype=dtype,
        return_total=return_total,
        return_per_exchange=return_per_exchange,
        ignore_missing=ignore_missing,
        project_name=project_name
    )


if __name__=='__main__':
    __spec__ = None
    lcia_CLI()