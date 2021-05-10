# Search-with-Prioritize
I created this project using Python.
Here I have used an algorithm that is quit similar to the backend of the Google search.
Here this program accepts number of lines as per the users demand and append those lines into a list.
Then displays all the accepted lines excluding the repetitions as it pops all the duplicates.
After this it asks the user to enter a keyword on the basis of which it searches the lines.
The mechanism of searching lines is that, when user enters some keyword, then my program intelligently counts the frequency of that keyword in each line.
If the frequency is zero then it simply display that no results found.
If one result is found then it shows that single result.
But if several number of results are found then, it shows the result that is most appropriate means the line that has the maximum frequency of that keyword.
Also it asks the user whether they are satisfied with that result or not,
if user is satisfied then program ends and it displays operation completed successfully.
But if user is not satisfied with the result then it displays the second most appropriate result and so on, till the user is satisfied.
If at last user is not satisfied with any of the result then again the program ends.
This is how my program looks like.
