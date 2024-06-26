from modelscope import AutoModelForCausalLM, AutoTokenizer

device = "cuda"
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen2-1.5B-Instruct",
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2-1.5B-Instruct")


class Ai:

    def __init__(self, system):
        self.messages = []
        if system is not None:
            self.messages.append({"role": "system", "content": system})

    @classmethod
    def init_none(cls):
        return cls(None)

    def dialogue(self, message):
        self.messages.append({"role": "user", "content": message})
        text = tokenizer.apply_chat_template(
            self.messages,
            tokenize=False,
            add_generation_prompt=True
        )
        model_inputs = tokenizer([text], return_tensors="pt").to(device)

        generated_ids = model.generate(
            model_inputs.input_ids,
            max_new_tokens=512
        )
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]

        response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        self.messages.append({"role": "assistant", "content": response})
        return response

    def reset(self):
        self.messages = []
