import os
import re
import shutil
import json
from typing import *
from pathlib import Path
from loguru import logger
from tqdm import tqdm


def move_file(from_path: Path, to_path: Path):
    shutil.copy(from_path, to_path)


def main(base_dir, group_size: int = 100, group_by_difficulty: bool = False):
    file_path_mapping = get_mapping_relation(base_dir, group_size, group_by_difficulty)
    for source in tqdm(file_path_mapping.keys(), 'Move File'):
        move_file(source, file_path_mapping[source])
    logger.success('------Move Successful--------')
    logger.info('----END-----')


def get_mapping_relation(base_dir, group_size: int = 100, group_by_difficulty: bool = False) -> Dict[Path, Path]:
    "获得 文件来源 和 去处的映射关系"
    file_path_mapping = {}
    failed_move_file_path = []
    for dir_path, dir_names, filenames in os.walk(base_dir):
        for filename in filenames:
            if filename.startswith('__'):
                continue
            source_path = Path(dir_path).joinpath(filename)
            move_path = None
            # 按 题号切分
            if group_by_difficulty == False:
                num_reg = re.compile('(\d+).py')
                match_result = num_reg.search(filename)
                if match_result:
                    number = int(match_result.groups()[0])
                    multi = number // group_size
                    move_path = Path('./tidy_job/group_size').joinpath(
                        f"{group_size * multi}-{group_size * (multi + 1)}")
                    if not move_path.exists():
                        move_path.mkdir(exist_ok=False, parents=True)
                    move_path.joinpath(filename)
                else:
                    failed_move_file_path.append(f"Filename Mast Match reg \d+.py _{str(source_path)}")
            # 按难度切分
            else:
                with open(source_path) as f:
                    content = f.read()
                    difficulty = re.compile('^#.*?difficulty.*?=(.*?)$')
                    reg_result = difficulty.search(content)
                    if reg_result:
                        difficulty = reg_result.groups()[0]
                        move_path = Path('./tidy_job/group_difficulty').joinpath(difficulty)
                        if not move_path.exists():
                            move_path.mkdir(exist_ok=False, parents=True)
                        move_path = move_path.joinpath(filename)
                    else:
                        failed_move_file_path.append(f"File content Mast have # difficulty = XXX ,{str(source_path)}")
            file_path_mapping[source_path] = move_path
    # move_error log
    if failed_move_file_path:
        temp_path = Path('./temp/logger')
        if not temp_path.exists():
            temp_path.mkdir(exist_ok=False, parents=True)
        logger_file_path = temp_path.joinpath('failed_move_file_path.json')
        with open(logger_file_path) as f:
            json.dump(failed_move_file_path, f, indent=2, ensure_ascii=False)
        logger.error(f'exist file move error:[{logger_file_path}]')
    logger.success("Get file move mapping info")
    return file_path_mapping


if __name__ == '__main__':
    base_dir = './warehouse_job'
    group_size = os.getenv('group_size', 100)
    group_by_difficulty = False

    if group_by_difficulty:
        main(base_dir, group_by_difficulty)
    else:
        main(base_dir, group_size)
