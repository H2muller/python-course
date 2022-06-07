from dataclasses import dataclass
'''
1
2
3
4
5
'''

@dataclass
class Module():
    module_name: str
    is_available: bool = False
    is_complete: bool = False

def update_module_availability(current_module: Module, next_module: Module) -> None:
    if current_module.is_complete:
        next_module.is_available = True
    return

def create_course_modules() -> None:
    list_of_modules: list = ['Unix File Structures',
                        'Process Monitoring in Unix',
                        'Introduction to Python',
                        'Advanced Operations in Python',
                        'Introduction to Data Science',
                        'Programming Best Practices']

    for i, module_name in enumerate(list_of_modules):
        if i == 0:
            Module(module_name, True, False)
        else:
            Module(module_name, False, False)
    return



