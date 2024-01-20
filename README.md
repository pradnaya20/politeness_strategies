# Team Processing Mapping Coding Task
Welcome to the coding task for the Team Process Mapping project! Before you begin, please make sure to read through the full instructions [here](https://docs.google.com/document/d/1_FZ-N-7Qr9_CXK-fX9vdcMhkaDzmRXyUh1aHEHjL1hs/edit).

## Packages and Requirements
The packages required for you to complete the task are listed in `requirements.txt`. You can use a virtual environment for managing the dependencies associated with this project.

## Your Goal
To complete this assignment, you will need to modify 4 different files:
- features/word_count.py: `count_words(text)`
- features/type_token_ratio.py: `get_word_ttr(text)`
- features/politeness_features.py: `get_politeness_strategies(text)`
- utils/calculate_chat_level_features.py (For calling the functions; you only need to modify `apply_politeness()`).

## Your Deliverables
At the end of Part 2, we will need the following:
- A link to your GitHub cloned repository. This should contain:
  1. Your Python code;
  2. Your Part 2 Reflection (directly edit this README!).
- A copy of your chat-level CSV that contains columns for the features you generated. **Note: this should be reproducible!** We should be able to get the same results by running your code from the GitHub link you submit.

# Part 2 Reflection
Please answer the following four questions:

## 1. Sanity Check
Open up your output CSV and look at the columns you generated for each of the three features. Do the values “make sense” intuitively? Why or why not?
> I checked the first two output columns (num_words and word_TTR) by taking a random selection of messages and counting the number of words then calculating the type-token ratio. Take for example the message in cell N133, "why do you guys keep moving them." This message has 7 words (cell P133) and 7 unique words. The type-token ratio is therefore 1 (cell Q133). I repeated this process for about 20 messages, confirming that the values make sense every time. This was relatively straightforward. The columns corresponding to the politeness features were more complicated. The first time I ran my code it did not output any columns for the politeness feature. I intuitively knew that it was wrong. It also ran too quickly, giving me the sense that something was missing. After iterating, the output displayed columns R to AL. In a similar way, I randomly selected messages and went through the values that correspond to them. Take for example the message in N10, "pay attention to the numbers if you care about  please." There is a 1 in R10, indicating that "please" exists in the message. There is a 0 in S10, indicating that "please" is not the first word of the message. There is a 0 in T10, indicating that the message does not have hedging. I continued this process for every column for about 20 messages as well. Given my intuitive and unconscious understanding of features like hedging, gratitude, and deference, I was able to confirm whether the values make sense to me. 

The human ability to understand verbal and non-verbal communication (and develop this understanding as we grow up) is what allows me to "intuitively" know whether a message is, say, polite or not. I wonder whether, if trained sufficiently, a model might be able to develop the same "intuition" -- identify patterns in messages that contain a given feature and use that pattern to sort new message based on those features. Personally, because language is constantly evolving (like how some words have different meanings in the sociocultural context from one day to the next), I doubt a model would be able to do this as well as a human, but perhaps it could under restricted parameters.

## 2. Testing
How would you implement tests for these features?
> I tested the first two features in the terminal by setting inputs and returning their outputs, and then confirming by counting the number of words or calculating the type-token ratio. I imagine that testing the third feature might be a little more complicated. Drawing on test-driven development strategies, I might include an "assert" function within the num_words feature, for example, to ensure that the feature works. Perhaps something similar might work for the third feature, though it would have to be tested such that it could go into a dictionary where the values merge and the strings are removed. I came across unittest.mock, a library for testing in Python that allows one to replace the system being tested with mock objects and make assertions about how they are being used. I could use it to isolate and test the behavior of my code without actually relying on ConvoKit's functionality. 

## 3. Overall Experience
Please provide an overall reflection of your experience. How did you approach this task? What challenge(s) did you encounter? Is there anything you would be curious to explore in the future, if you had more time?
> I find this work really exciting, and my interest in the project definitely propelled me throughout the task. I began by reading. I started by reading the task document a few times. First to grasp the challenge at hand, and then to really familiarize myself with the codebase and thoroughly understand the features. Then, I read through the README in the GitHub repository. At this point, I took my first stab at coding, starting with the first feature. I began with using a function I was familiar with, and then Googled alternative ways to count the number of words in a string. This gave me a few options. I tested them out in the terminal by inputting values for "text" and then checking the output. I then moved on to the second task and followed a similar process, all the while referencing websites, Reddits, Stack Overflow, blogs, and other documentation. Before starting the third feature, I took some time to read through the documentation provided in the task document. I looked at a first example and tried to adapt it for this context. I coded side-by-side with examples on GitHub and from other sources. I tried to keep an iterative process, constantly testing out the code and then editing or scrapping it if it didn't output the correct values. 

I found the third feature to be extremely challenging. In hindsight, I feel that reading through the documentation a few times and then thoroughly understanding a few examples before starting to code might have sped up my process. Unfortunately, my impatience meant that I often made errors I might have avoided if I had read all the examples before starting. That said, it was an interesting (and frustrating) learning experience and I imagine these techniques will stick in my head better this way, so I guess it's a bit of a trade off. Once I read through enough examples I was able to put together a solution that seemed to work well. I found that having a specific project and goal in mind while coding was very grounding for me. Sometimes, when learning to code without context, like through a random exercise, I find myself losing motivation and purpose. I found this task to be really interesting, and even though feature 3 was especially frustrating, understanding the purpose for the output compelled me to think about creative solutions.

I'm curious to further explore the uses of the ConvoKit. I wonder about what insights might come of exploring patterns in the metadata. The example of the Reddit-specific metadata is especially interesting in light of the data labeling task. For instance, how might the number of downvotes on a post relate with the writer's subversion? Perhaps they feel more defensive the more downvotes they receive and this leads them to undermine others more often? I'd be interested in looking more into this.


## 4. Time Required
How much time did it take you to complete Parts 1 and 2? (Please be honest; we are looking for feedback to make sure the tasks are scoped appropriately.)
> Part 1 took me 20 minutes. Part 2 took about 16 hours. It's been a while since I last worked with Python and I spent quite a bit of time re-familiarizing myself with the syntax. I also spent a fair bit of time reading through documentation to understand how ConvoKit works. I ended up with incorrect outputs a few times as well, so I did lots of iteration.
