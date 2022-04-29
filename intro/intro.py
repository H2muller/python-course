from dataclasses import dataclass

'''
 $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\        $$\   $$\  $$$$$$\   $$$$$$\  
$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\       $$ |  $$ |$$  __$$\ $$  __$$\ 
$$ /  \__|$$ |  $$ |$$ /  \__|$$ /  \__|      $$ |  $$ |$$ /  $$ |$$ /  $$ |
$$ |      $$$$$$$  |\$$$$$$\  $$ |            $$$$$$$$ |\$$$$$$$ |\$$$$$$$ |
$$ |      $$  ____/  \____$$\ $$ |            \_____$$ | \____$$ | \____$$ |
$$ |  $$\ $$ |      $$\   $$ |$$ |  $$\             $$ |$$\   $$ |$$\   $$ |
\$$$$$$  |$$ |      \$$$$$$  |\$$$$$$  |            $$ |\$$$$$$  |\$$$$$$  |
 \______/ \__|       \______/  \______/             \__| \______/  \______/

   ___       __  __                  ___        
  / _ \__ __/ /_/ /  ___  ___       / _/__  ____
 / ___/ // / __/ _ \/ _ \/ _ \     / _/ _ \/ __/
/_/   \_, /\__/_//_/\___/_//_/    /_/ \___/_/   
     /___/
   ___  _      _      ___                    __  _       
  / _ )(_)__  (_)__  / _/__  ______ _  ___ _/ /_(_)______
 / _  / / _ \/ / _ \/ _/ _ \/ __/  ' \/ _ `/ __/ / __(_-<
/____/_/\___/_/_//_/_/ \___/_/ /_/_/_/\_,_/\__/_/\__/___/
'''

@dataclass
class courseInfo():
    '''
    This class stores the CPSC499 course info
    '''
    prof_name: str = 'Dr. Hans Müller Paul'
    prof_email: str = 'hmpaul2@illinois.edu'
    course_dept: str = 'CPSC'
    course_number: int = 499
    course_semester: str = 'Asynchronous'
    def __str__(self) -> str:
        return ' '.join([
                        'Welcome to ',
                        self.course_dept,
                        str(self.course_number),
                        'I am ',
                        self.prof_name,
                        'and you can contact me at ',
                        self.prof_email,
                        '. This is an ',
                        self.course_semester,
                        ' course.'
                        ])

def main():
    return

if __name__ == '__main__':
    main()