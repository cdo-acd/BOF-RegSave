from typing import List, Tuple

from outflank_stage1.task.base_bof_task import BaseBOFTask
from outflank_stage1.task.enums import BOFArgumentEncoding


class RegdumpBOF(BaseBOFTask):
    def __init__(self):
        super().__init__("hashdump", base_binary_name="regdump")

        self.parser.description = (
            "BOF to dump SAM, SYSTEM, and SECURITY Reg keys to disk"
        )
        self.parser.epilog = "Usage: hashdump <PATH>"

        self.parser.add_argument(
            "path",
            help=f"Path to write SAM, SYSTEM, and SECURITY files to"        
        )

    def _encode_arguments_bof(
        self, arguments: List[str]
    ) -> List[Tuple[BOFArgumentEncoding, str]]:
        parser_arguments = self.parser.parse_args(arguments)

        return [(BOFArgumentEncoding.STR, parser_arguments.path)]
