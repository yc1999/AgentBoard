import json
import os
from agents.vanilla_agent import VanillaAgent

class ToolDataset:
    def __init__(self, test_file) -> None:
        super().__init__()
        self._load_data(test_file)

    def _load_data(self, test_file_path):
        
        data = None
        with open(test_file_path, "r") as f:
            data = [json.loads(line) for line in f.readlines()]

        self.goals = [ i["goal"] for i in data ] 
        
        if "answer" in data[0]["additional_info"]:
            self.ground_truths = [ i["additional_info"]["answer"] for i in data ]

        if "subgoals" in data[0]:
            self.ground_truth_subgoals = [ i["subgoals"] for i in data ]

        if "init_config" in data[0]["additional_info"]: 
            self.init_configs = [ i["additional_info"]["init_config"] for i in data ]
        
        if "goal_type" in data[0]["additional_info"]: 
            self.goal_types = [ i["additional_info"]["goal_type"] for i in data ]

        if "tool" in data[0]["additional_info"]: 
            self.tools = [ i["additional_info"]["tool"] for i in data ]
        
        if "difficulty" in data[0]:
            self.difficulties = [ i["difficulty"] for i in data ]
        
    def __len__(self):
        return len(self.goals)

    def write_result(self, id, question, ground_truth, agent, success, steps, progress_rate, output, grounding_acc, score_change_record):
        action_path = agent.memory
        item = {
            "id": id,
            "question": question,
            "steps": steps,
            "success": success,
            "progress_rate": progress_rate,
            "output": output,
            "ground_truth_output": ground_truth,
            "action_path": action_path,
            "grounding_acc": grounding_acc,
            "score_change_record": score_change_record,
        }

        self.results = []
        self.results.append(item)

        with open( os.environ["PROJECT_PATH"] + "/trajectory/results.json", "w") as f:
            json.dump(self.results, f, indent=4, ensure_ascii=False)