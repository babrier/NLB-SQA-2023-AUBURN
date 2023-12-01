## NLB Project Report Markdown File

- Ben Brierly - I completed task 4.a which created a githook to run and
  report all security weaknesses in the project in a CSV file. The githook
  was created in a modiffied pre-commit file that used bandit to reccurssively
  select and analyze all python files. The resulting analysis was placed in a
  csv where a vareity of issues were found including hardcoded passwords,
  processes having partial executable paths, and subprocesses without shells.
  From doing this I gained an understanding of the value of modifiying
  githooks, in that, one static analysis tool (like bandit) can prevent pushing
  vulnerable software to production which otherwise could go unnoticed by developers.
  
- Liam Hussey - I performed task 4.b where I created a fuzz.py file that 
fuzzed five methods for potential vulnerabilities
(isValidUserName, isValidPasswordName, isValidKey, readYAMLAsStr, getYAMLFiles).
During this testing I found that all five methods had some form of vulnerability regarding
the improper functioning of the method when given an input that is supposed to be 
invalid, such as accepting the wrong file types or accepting usernames that go against common 
practice. The most important lesson I learned while deploying these tests is that you can 
thoughtfully design security into your code and there will still be vulnerabilities that you 
did not take into account. That is why it is important to have a process such as fuzzing in 
order to catch and eliminate harmful vulnerabilities in your code.

* Nolan Evans - Task: 4.c
  * Added forensics to 5 methods in parser.py: getValsFromKey(), loadMultiYAML(), checkParseError(), find_json_path_keys(), update_json_paths(). Logs focus on tracking the flow of the program, logging data as it is manipulated, and logging erros/exceptions.
  * Made logger.py, which uses the logging package to initalize a logger. logger.py adds all logs to the logs subdirectory.
  * Lesson learned: logging is a useful tool for debugging, because we have a record of when things go wrong and where they went wrong. Adding logs is fairly simple to do, and is extremly useful for analysis of a tools performance.

