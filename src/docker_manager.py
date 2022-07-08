import docker
client = docker.DockerClient(base_url='unix://var/run/docker.sock')


class DockerManager():
    def __init__(self) -> None:
        pass

    def get_all_containers(self):
        return client.containers.list(all=True)
    
    def container_status(self, status):
        if status == "running":
            return "▶️"
        elif status == "exited":
            return "⏹️"
        elif status == "paused":
            return "⏸️"

    def start_container(self, container_id: str):
        client.containers.get(container_id=container_id).start()
        return True
    
    def pause_container(self, container_id: str):
        client.containers.get(container_id=container_id).pause()
        return True
        
    def stop_container(self, container_id: str):
        client.containers.get(container_id=container_id).stop()
        return True
    
    def restart_container(self, container_id: str):
        client.containers.get(container_id=container_id).restart()
        return True
    