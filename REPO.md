## NLB Project Report Markdown File
- Ben Brierly - I performed task 4.a which created a githook to run and
  report all security weaknesses in the project in a CSV file. The githook
  was created in a modiffied pre-commit file that used bandit to reccurssively
  select and analyze all python files. The resulting analysis was placed in a
  csv where a vareity of issues were found including hardcoded passwords and
  processes having partial executable paths.

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

