from typing import List
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from src.docker_manager import DockerManager

docker_manager = DockerManager()

class KeyboardCreator:
    def __init__(self) -> None:
        pass

    def build_keyboard(self, current_list: List[str]) -> InlineKeyboardMarkup:
        """Helper function to build the next inline keyboard."""
        if len(current_list) == 0:
            return self.main_menu(current_list=current_list)

        if len(current_list) == 1 and current_list[0] == "containers":
            return InlineKeyboardMarkup.from_column(
                [
                    InlineKeyboardButton(
                        docker_manager.container_status(status=container.status) + str(container.short_id + " [" + container.name + "]"), callback_data=(container.short_id, current_list)
                        ) for container in docker_manager.get_all_containers()
                ]
            )

        if len(current_list) == 2 and current_list[0] == "containers":
            return InlineKeyboardMarkup.from_column(
                [InlineKeyboardButton(str("Start"), callback_data=("start", current_list)),
                InlineKeyboardButton(str("Pause"), callback_data=("pause", current_list)),
                InlineKeyboardButton(str("Stop"), callback_data=("stop", current_list)),
                InlineKeyboardButton(str("Restart"), callback_data=("restart", current_list)),
                ]
            )

        if len(current_list) == 3 and current_list[0] == "containers":
            if current_list[2] == "start":
                docker_manager.start_container(container_id=current_list[1])
            if current_list[2] == "pause":
                docker_manager.pause_container(container_id=current_list[1])
            if current_list[2] == "stop":
                docker_manager.stop_container(container_id=current_list[1])
            if current_list[2] == "restart":
                docker_manager.restart_container(container_id=current_list[1])
            return self.main_menu(current_list=[])


    def main_menu(self, current_list: List[str]):
        return InlineKeyboardMarkup.from_column(
                [
                InlineKeyboardButton(str("Containers"), callback_data=("containers", current_list)),
                ]
            )