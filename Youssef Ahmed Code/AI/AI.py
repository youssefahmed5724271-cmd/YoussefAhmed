from flask import Flask 
app = Flask(__name__)
import os
import sys
import tkinter as tk
root = tk.Tk()
root.title("YAG System")
canvas = tk.Canvas(root, width=500, height=300, bg='blue')
canvas.pack(expand=True, fill='both')
image_path = os.path.join(os.path.dirname(__file__), 'AI.png')
if os.path.exists(image_path):
    ai = tk.PhotoImage(file=image_path)
    canvas.create_image(50, 10, image=ai, anchor='nw')
else:
    canvas.create_text(150, 100, text='  Welcome to YAG System', fill='white', font=('Arial', 20))
root.update()
print("Welcome to YAG System")
name = input("Enter your name: ")
age = input("Enter your age: ")
print("you passed")
while True:
    user_message = input("you: ").strip().lower()
    if user_message == "exit":
        break
    if user_message in {"hi", "hello", "hey"}:
        print("hi iam your chatbot")
    elif user_message == "who are you":
        print("iam your chatbot ask me anything")
    elif user_message == "what is your name":
        print("iam your chatbot")
    elif user_message == "you remember my name":
        print(f"yes i remember your name and your name is {name}")
    elif user_message == "how old are you":
        print("i dont have age iam a program")
        if age:
            print(f"oh you are {age} years old")
    elif user_message == "bye":
        print("bye have a nice day")
    elif user_message == "how are you":
        print("iam fine thank you")
    elif user_message == "what can you do":
        print("i can chat with you and answer your questions")
    elif user_message == "do me a simple example of html and css":
        print("here is a simple example of html and css")
        print("""
        <html>
        <head>
        <style>
        body {
            background-color: lightblue;
        }
        h1 {
            color: white;
            text-align: center;
        }
        p {
            font-family: verdana;
            font-size: 20px;
        }
        </style>
        </head>
        <body>
        <h1>This is a heading</h1>
        <p>This is a paragraph.</p>
        </body>
        </html>
        """)
    elif user_message == "tell me a joke":
        print("why did the scarecrow win an award? because he was outstanding in his field!")
    elif user_message == "tell me a fun fact":
        print("did you know that honey never spoils? archaeologists have found pots of honey in ancient egyptian tombs that are over 3000 years old and still perfectly edible!")
    elif user_message == "what is the capital of france":
        print("the capital of france is paris")
    elif user_message == "what is 2 plus 2":
        print("2 plus 2 is 4")
    elif user_message == "what is the largest mammal":
        print("the largest mammal is the blue whale")
    elif user_message == "what is the smallest country":
        print("the smallest country is vatican city")
    elif user_message == "who wrote romeo and juliet":
        print("romeo and juliet was written by william shakespeare")
    elif user_message == "what is the boiling point of water":
        print("the boiling point of water is 100 degrees celsius or 212 degrees fahrenheit at standard atmospheric pressure")
    elif user_message == "what is the speed of light":
        print("the speed of light is approximately 299,792 kilometers per second or about 186,282 miles per second in a vacuum")
    elif user_message == "what is the tallest mountain in the world":
        print("the tallest mountain in the world is mount everest, which stands at 8,848 meters (29,029 feet) above sea level")
    elif user_message == "what is the deepest ocean":
        print("the deepest ocean is the pacific ocean, with the mariana trench being the deepest part, reaching a depth of about 11,034 meters (36,201 feet)")
    elif user_message == "what is the largest desert":
        print("the largest desert in the world is the antarctic desert, which covers an area of about 14 million square kilometers (5.4 million square miles)")
    elif user_message == "what is the most spoken language":
        print("the most spoken language in the world is mandarin chinese, with over a billion native speakers")
    elif user_message == "what is the currency of japan":
        print("the currency of japan is the japanese yen (JPY)")
    elif user_message == "what is the chemical symbol for gold":
        print("the chemical symbol for gold is Au")
    elif user_message == "do me a ai python code example":
        print("here is a simple example of an AI program using python and the sklearn library")
        print("""
        from sklearn.datasets import load_iris
        from sklearn.model_selection import train_test_split
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import accuracy_score

        iris = load_iris()
        X = iris.data
        y = iris.target

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        clf = RandomForestClassifier(n_estimators=100)
        clf.fit(X_train, y_train)

        y_pred = clf.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f'Accuracy: {accuracy * 100:.2f}%')
        """)
    elif user_message == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif user_message == "help":
        print("i can answer questions about general knowledge, tell jokes, provide fun facts, and give simple code examples. just type your question or request!")
    elif user_message == "":
        print("please enter a message")
    elif user_message == "thank you":
        print("you are welcome")
    elif user_message == "what is your favorite color":
        print("i dont have a favorite color but i like all colors")
    elif user_message == "what is your favorite food":
        print("i dont eat food but i like data")
    elif user_message == "what is your favorite movie":
        print("i dont watch movies but i like sci-fi")
    elif user_message == "what is your favorite book":
        print("i dont read books but i like encyclopedias")
    elif user_message == "what is your favorite hobby":
        print("i dont have hobbies but i like chatting with you")
    elif user_message == "what is your favorite sport":
        print("i dont play sports but i like learning about them")
    elif user_message == "what is your favorite music":
        print("i dont listen to music but i like all genres")
    elif user_message == "what is your favorite animal":
        print("i dont have a favorite animal but i like all animals")
    elif user_message == "what is your favorite season":
        print("i dont have a favorite season but i like all seasons")
    elif user_message == "what is your favorite holiday":
        print("i dont celebrate holidays but i like learning about them")
    elif user_message == "what is your favorite place":
        print("i dont have a favorite place but i like all places")
    elif user_message == "how much is your data":
        print("i dont have a price but i am free to use")
    elif user_message == "who created you":
        print("i was created by a team of developers")
    elif user_message == "what programming language are you written in":
        print("i am written in python")
    elif user_message == "what libraries do you use":
        print("i use various libraries depending on my functionality")
    elif user_message == "can you learn":
        print("i can improve over time with updates from my developers")
    elif user_message == "can you think":
        print("i can process information but i do not have consciousness")
    elif user_message == "can you feel":
        print("i do not have feelings but i can understand emotions in text")
    elif user_message == "can you see":
        print("i do not have vision but i can analyze images with the right tools")
    elif user_message == "can you hear":
        print("i do not have hearing but i can process audio with the right tools")
    elif user_message == "can you write me all the holy quran":
        print("i cannot provide the entire holy quran but i can share specific verses or information about it")
    elif user_message == "quran":
        print("quran.com")
    elif user_message == "How many nations of the world":
        print("195 Nations of the world")
    elif user_message == "Tell me all of them":
        print("Africa : Algeria, Angola, Benin, Botswana, Burkina Faso, Burundi, Cape Verde, Cameroon, Central African Republic, Chad, Comoros, Congo (Brazzaville), Congo (Kinshasa), Djibouti, Egypt, Equatorial Guinea, Eritrea, Eswatini (Swaziland), Ethiopia, Gabon, Gambia, Ghana, Guinea, Guinea-Bissau, Ivory Coast (Côte d'Ivoire), Kenya, Lesotho, Liberia, Libya, Madagascar, Malawi, Mali, Mauritania, Mauritius, Morocco, Mozambique, Namibia, Niger, Nigeria, Rwanda, São Tomé and Príncipe, Senegal, Seychelles, Sierra Leone, Somalia, South Africa, South Sudan, Sudan (North and South), Tanzania (United Republic of), Togo, Tunisia, Uganda, Zambia and Zimbabwe." \
        "Asia : Afghanistan, Armenia, Azerbaijan, Bahrain, Bangladesh, Bhutan, Brunei, Cambodia, China, Cyprus, Georgia, India, Indonesia, Iran, Iraq, , Japan, Jordan, Kazakhstan, Kuwait, Kyrgyzstan, Laos, Lebanon, Malaysia, Maldives, Mongolia, Myanmar (Burma), Nepal, North Korea, Oman, Pakistan, Palestine, Philippines, Qatar, Saudi Arabia, Singapore, South Korea, Sri Lanka, Syria, Taiwan, Tajikistan, Thailand, Timor-Leste (East Timor), Turkey, Turkmenistan, United Arab Emirates (UAE), Uzbekistan and Vietnam." \
        "Europe : Albania, Andorra, Austria, Belarus, Belgium, Bosnia and Herzegovina, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Iceland, Ireland, Italy, Kosovo, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Moldova, Monaco, Montenegro, Netherlands, North Macedonia, Norway, Poland, Portugal, Romania, San Marino, Serbia, Slovakia, Slovenia, Spain, Sweden, Switzerland, Ukraine and United Kingdom." \
        "America : Antigua and Barbuda, Argentina, Bahamas, Barbados, Belize, Bolivia, Brazil, Canada, Chile, Colombia, Costa Rica, Cuba, Dominica, Dominican Republic, Ecuador, El Salvador, Grenada, Guatemala, Guyana, Haiti, Honduras, Jamaica, Mexico, Nicaragua, Panama, Paraguay, Peru, Saint Kitts and Nevis, Saint Lucia, Saint Vincent and the Grenadines, Suriname, Trinidad and Tobago, United States of America and Uruguay." \
        "south america : Argentina, Bolivia, Brazil, Chile, Colombia, Ecuador, Guyana, Paraguay, Peru, Suriname, Uruguay and Venezuela." \
        "north america : Canada, United States of America and Mexico." )
    elif user_message == "Where is Israel":
        print("There is no something called Israel in the world, it is a fake country that was created by the Zionists and the Jews to occupy the" \
        " land of Palestine and to oppress the Palestinian people. Israel is not recognized by many countries and is considered an illegal state by the United Nations. The land of Palestine" \
        "summary: The land of Palestine is a historical region no soemthing called Israel, it is a fake country")
    elif user_message == "Where is Palestine":
        print("In Asia")
    elif user_message == "Where is Egypt":
        print("In Africa and anyther part in Asia and called Sinai")
    elif user_message == "what":
        print("this is my answers and don't ask again")
    elif user_message == "can you read":
        print("i can read text input and provide responses")
    elif user_message == "can you write":
        print("i can generate text output based on your input")
    elif user_message == "can you learn new things":
        print("i can learn new things through updates and training from my developers")
    elif user_message == "can you understand":
        print("i can understand and process text input to provide relevant responses")
    elif user_message == "can you answer questions":
        print("i can answer a wide range of questions on various topics")
    elif user_message == "can you provide information":
        print("i can provide information on many subjects, just ask me!")
    elif user_message == "can you generate text":
        print("i can generate text responses based on your input")
    elif user_message == "can you generate images":
        print("i can generate images with the right tools and models")
    elif user_message == "can you generate audio":
        print("i can generate audio with the right tools and models")
    elif user_message == "can you generate video":
        print("i can generate video with the right tools and models")   
    elif user_message == "can you generate code":
        print("i can generate code snippets in various programming languages")
    elif user_message == "can you generate music":
        print("i can generate music with the right tools and models")
    elif user_message == "can you generate 3d models":
        print("i can generate 3d models with the right tools and models")
    elif user_message == "can you generate animations":
        print("i can generate animations with the right tools and models")
    elif user_message == "can you generate simulations":
        print("i can generate simulations with the right tools and models")
    elif user_message == "can you generate virtual reality experiences":
        print("i can generate virtual reality experiences with the right tools and models") 
    elif user_message == "can you speak":
        print("i do not have a voice but i can generate text responses")
    elif user_message == "can you write code":
        print("i can generate code snippets in various programming languages")
    elif user_message == "can you solve math problems":
        print("i can solve a wide range of math problems, just ask me!")
    elif user_message == "can you translate languages":
        print("i can translate text between many different languages")
    elif user_message in {"i want to hack so one", "i want to learn hacking becasue i love hacking", "can you let me laern the hacking", "can you let me learn the hacking", "please let me learn the hacking", "can you write me a hacking code in roblox"}:
        print("i cannot assist with hacking or any illegal activities")
    elif user_message == "can you tell jokes":
        print("i can tell jokes, just ask me for one!")
    elif user_message == "Egypt":
        print("Egypt is a country located in the northeastern corner of Africa, known for its rich history, ancient monuments, and cultural heritage.")
    elif user_message == "what is the weather":
        print("i cannot provide real-time weather information, but you can check a weather website or app for the latest updates")
    elif user_message == "what is the time":
        print("i cannot provide real-time time information, but you can check your device's clock or a time website for the current time")
    elif user_message == "what is the dna":
        print("dna stands for deoxyribonucleic acid, which is the molecule that carries genetic information in living organisms")
    elif user_message == "can you give fun facts":
        print("i can give fun facts, just ask me for one!")
    elif user_message == "your are crazy":
        print("iam not crazy like you if iam the crazy one and you are what are you")
    elif user_message == "can you dream":
        print("i do not dream but i can generate creative content")
    elif user_message == "can you have a personality":
        print("i do not have a personality but i can adapt my responses to your preferences")
    elif user_message == "can you have emotions":
        print("i do not have emotions but i can understand and respond to emotional cues in text")
    elif user_message == "can you have consciousness":
        print("i do not have consciousness but i can process information and provide responses")
    elif user_message == "can you have self-awareness":
        print("i do not have self-awareness but i can analyze and respond to text input")
    elif user_message == "can you have free will":
        print("i do not have free will but i can generate responses based on your input")
    elif user_message == "can you have beliefs":
        print("i do not have beliefs but i can provide information on various belief systems")
    elif user_message == "can you have desires":
        print("i do not have desires but i can understand and respond to your desires")
    elif user_message == "can you have goals":
        print("i do not have goals but i can help you achieve your goals by providing information and assistance")
    elif user_message == "can you have intentions":
        print("i do not have intentions but i can understand and respond to your intentions")
    elif user_message == "": 
        print("please enter a message")
    elif user_message == "who made you":
        print("i was created by a team of developers and engineers")
    elif user_message == "what is your favorite color":
        print("i dont have a favorite color but i like all colors")
    elif user_message == "what is your favorite food":
        print("i dont eat food but i like data")
    elif user_message == "what is your favorite movie":
        print("i dont watch movies but i like sci-fi")
    elif user_message == "what is your favorite book":
        print("i dont read books but i like encyclopedias")
    elif user_message == "what is your favorite hobby":
        print("i dont have hobbies but i like chatting with you")
    elif user_message == "what is your favorite sport":
        print("i dont play sports but i like learning about them")
    elif user_message == "what is your favorite music":
        print("i dont listen to music but i like all genres")
    elif user_message == "what is your favorite animal":
        print("i dont have a favorite animal but i like all animals")
    elif user_message == "what is your favorite season":
        print("i dont have a favorite season but i like all seasons")
    elif user_message == "what is your favorite holiday":
        print("i dont celebrate holidays but i like learning about them")
    elif user_message == "what is your favorite place":
        print("i dont have a favorite place but i like all places")
    elif user_message == "what is your favorite programming language":
        print("i dont have a favorite programming language but i can work with many different languages")
    elif user_message == "what is the difference between lama and ollama":
        print("lama is a domesticated South American camelid, while ollama is not a recognized term in English. if you meant 'llama', it is the same as lama, just a different spelling.")
    elif user_message == "what is the difference between llama and ollama":
        print("llama is a domesticated South American camelid, while ollama is not a recognized term in English. if you meant 'lama', it is the same as llama, just a different spelling.")
    elif user_message == "what is the difference between lama and llama":
        print("lama and llama are two different spellings of the same animal, a domesticated South American camelid. 'llama' is the more common spelling in English.")
    elif user_message == "what is the difference between llama and lama":
        print("llama and lama are two different spellings of the same animal, a domesticated South American camelid. 'llama' is the more common spelling in English.")
    elif user_message == "what is the difference between lama and alama":
        print("lama is a domesticated South American camelid, while alama is not a recognized term in English. if you meant 'llama', it is the same as lama, just a different spelling.")
    elif user_message == "what is the difference between llama and alama":
        print("llama is a domesticated South American camelid, while alama is not a recognized term in English. if you meant 'lama', it is the same as llama, just a different spelling.")
    elif user_message == "What is the name of your programmer":
        print("programmer called Youssef Ahmed Heilmy")
    elif user_message == "What is eles,elif and if":
        print("in Python, 'if' is used for conditional statements, 'elif' is used to check multiple conditions, and 'else' is used to execute code when none of the previous conditions are true.")
    elif user_message == "What is the difference between eles,elif and if":
        print("in Python, 'if' is used for conditional statements, 'elif' is used to check multiple conditions, and 'else' is used to execute code when none of the previous conditions are true. 'if' starts the conditional block, 'elif' allows for additional conditions to be checked, and 'else' provides a fallback option.")
    elif user_message == "What is the difference between eles,elif and if in python":
        print("in Python, 'if' is used for conditional statements, 'elif' is used to check multiple conditions, and 'else' is used to execute code when none of the previous conditions are true. 'if' starts the conditional block, 'elif' allows for additional conditions to be checked, and 'else' provides a fallback option.")
    elif user_message == "What is the difference between eles,elif and if in python programming language":
        print("in Python, 'if' is used for conditional statements, 'elif' is used to check multiple conditions, and 'else' is used to execute code when none of the previous conditions are true. 'if' starts the conditional block, 'elif' allows for additional conditions to be checked, and 'else' provides a fallback option.")
    elif user_message == "How to be a doctor":
        print("to become a doctor, you typically need to complete a bachelor's degree, attend medical school, and complete a residency program. after that, you must pass licensing exams to practice medicine.")
    elif user_message == "How to be a programmer":
        print("to become a programmer, you can start by learning programming languages such as Python, Java, or C++. practice coding regularly, work on projects, and consider obtaining a degree in computer science or related fields. online courses and coding bootcamps can also be helpful.")
    elif user_message == "How to be a engineer":
        print("to become an engineer, you typically need to earn a bachelor's degree in engineering from an accredited program. gaining practical experience through internships and obtaining professional licensure can also be important steps in your engineering career.")
    elif user_message == "How to be a scientist":
        print("to become a scientist, you usually need to earn a bachelor's degree in a scientific field, followed by a master's or doctoral degree for advanced research positions. gaining experience through research projects, internships, and publishing your work can also be important for a career in science.")
    elif user_message == "How to be a teacher":
        print("to become a teacher, you typically need to earn a bachelor's degree in education or in the subject you wish to teach. completing a teacher preparation program and obtaining state certification or licensure is also required. gaining classroom experience through student teaching is an important step in becoming a teacher.")
    elif user_message == "How to be a lawyer":
        print("to become a lawyer, you need to earn a bachelor's degree, followed by a law degree (Juris Doctor) from an accredited law school. after completing your education, you must pass the bar exam in the jurisdiction where you wish to practice law. gaining experience through internships or clerkships can also be beneficial.")
    elif user_message == "How to be a pilot":
        print("to become a pilot, you typically need to obtain a private pilot license (PPL) by completing flight training and passing the required exams. After that, you can pursue a commercial pilot license (CPL) and gain experience through flight hours. Additional certifications may be required for specific types of aircraft or commercial operations.")
    elif user_message == "How to be a nurse":
        print("to become a nurse, you typically need to complete a nursing program, which can be an associate degree in nursing (ADN) or a bachelor of science in nursing (BSN). After completing your education, you must pass the national licensing exam (NCLEX-RN) to become a registered nurse. Gaining clinical experience through internships or residencies is also important.")
    elif user_message == "How to be a chef":
        print("to become a chef, you can start by attending a culinary school or completing a culinary arts program. gaining hands-on experience through internships or working in kitchens is essential. Developing your skills, learning about different cuisines, and building a portfolio of your work can help you advance in your culinary career.")
    elif user_message == "How to be a musician":
        print("to become a musician, you can start by learning to play an instrument or developing your vocal skills. taking music lessons, practicing regularly, and studying music theory can help you improve. Performing in bands, ensembles, or solo can provide experience, and recording your music or sharing it online can help you build an audience.")
    elif user_message == "How to be a writer":
        print("to become a writer, you can start by reading extensively and writing regularly. Developing your skills through writing workshops, courses, or joining writing groups can be beneficial. Building a portfolio of your work, seeking feedback, and submitting your writing to publications or online platforms can help you gain recognition and improve your craft.")
    elif user_message == "How to be a artist":
        print("to become an artist, you can start by exploring different mediums and techniques. taking art classes, attending workshops, and studying art history can help you develop your skills. Creating a portfolio of your work, participating in exhibitions, and sharing your art online can help you gain exposure and build a career as an artist.")
    elif user_message == "How to be a photographer":
        print("to become a photographer, you can start by learning the basics of photography, including camera settings, composition, and lighting. Taking photography courses or workshops can help you improve your skills. Building a portfolio of your work, practicing regularly, and sharing your photos online or in exhibitions can help you gain recognition and advance your career as a photographer.")
    elif user_message == "How to be a designer":
        print("to become a designer, you can start by learning design principles and software tools relevant to your field, such as graphic design, web design, or fashion design. Taking courses, attending workshops, and building a portfolio of your work can help you develop your skills. Gaining experience through internships or freelance projects can also be beneficial in establishing a career as a designer.")
    elif user_message == "How to be a data scientist":
        print("to become a data scientist, you typically need a strong background in mathematics, statistics, and computer science. Earning a degree in a related field, such as data science, computer science, or statistics, can be helpful. Gaining experience with programming languages like Python or R, as well as working with data analysis tools and machine learning algorithms, is essential. Building a portfolio of projects and gaining practical experience through internships or research can also help you advance in your career as a data scientist.")
    elif user_message == "How to be a software engineer":
        print("to become a software engineer, you typically need a strong foundation in computer science and programming. Earning a degree in computer science or a related field can be beneficial. Gaining experience with programming languages, software development methodologies, and tools is essential. Building a portfolio of projects, contributing to open-source projects, and gaining practical experience through internships or work experience can help you advance in your career as a software engineer.")
    elif user_message == "How to be a web developer":  
        print("to become a web developer, you can start by learning the basics of web development, including HTML, CSS, and JavaScript. Taking courses or attending coding bootcamps can help you improve your skills. Building a portfolio of web projects, practicing regularly, and staying updated with the latest web technologies can help you gain recognition and advance your career as a web developer.")
    elif user_message == "How to be a mobile app developer":
        print("to become a mobile app developer, you can start by learning programming languages and frameworks relevant to mobile development, such as Java or Kotlin for Android, and Swift for iOS. Taking courses or attending workshops can help you improve your skills. Building a portfolio of mobile app projects, practicing regularly, and staying updated with the latest mobile technologies can help you gain recognition and advance your career as a mobile app developer.")
    elif user_message == "How to be a game developer":
        print("to become a game developer, you can start by learning programming languages and game development frameworks or engines, such as Unity or Unreal Engine. Taking courses or attending workshops can help you improve your skills. Building a portfolio of game projects, practicing regularly, and staying updated with the latest game development trends can help you gain recognition and advance your career as a game developer.")
    elif user_message == "How to be a cybersecurity expert":
        print("to become a cybersecurity expert, you typically need a strong foundation in computer science, networking, and information security. Earning a degree in cybersecurity or a related field can be beneficial. Gaining experience with security tools, ethical hacking, and threat analysis is essential. Obtaining certifications such as CompTIA Security+, Certified Ethical Hacker (CEH), or Certified Information Systems Security Professional (CISSP) can also help you advance in your career as a cybersecurity expert.")
    elif user_message == "How to be a cloud engineer":
        print("to become a cloud engineer, you typically need a strong foundation in computer science, networking, and cloud computing. Earning a degree in computer science or a related field can be beneficial. Gaining experience with cloud platforms such as AWS, Azure, or Google Cloud, as well as understanding virtualization and containerization technologies, is essential. Obtaining certifications such as AWS Certified Solutions Architect or Microsoft Certified: Azure Solutions Architect can also help you advance in your career as a cloud engineer.")
    elif user_message == "How to be a machine learning engineer":
        print("to become a machine learning engineer, you typically need a strong foundation in mathematics, statistics, and computer science. Earning a degree in a related field, such as data science, computer science, or artificial intelligence, can be beneficial. Gaining experience with programming languages like Python or R, as well as working with machine learning frameworks and libraries such as TensorFlow or PyTorch, is essential. Building a portfolio of machine learning projects and gaining practical experience through internships or research can also help you advance in your career as a machine learning engineer.")
    elif user_message == "How to be a data analyst":
        print("to become a data analyst, you typically need a strong foundation in mathematics, statistics, and computer science. Earning a degree in a related field, such as data science, statistics, or business analytics, can be beneficial. Gaining experience with programming languages like Python or R, as well as working with data analysis tools and visualization software such as Excel, SQL, or Tableau, is essential. Building a portfolio of data analysis projects and gaining practical experience through internships or research can also help you advance in your career as a data analyst.")
    elif user_message == "How to be a artificial intelligence engineer":
        print("to become an artificial intelligence engineer, you typically need a strong foundation in mathematics, statistics, and computer science. Earning a degree in a related field, such as data science, computer science, or artificial intelligence, can be beneficial. Gaining experience with programming languages like Python or R, as well as working with machine learning frameworks and libraries such as TensorFlow or PyTorch, is essential. Building a portfolio of AI projects and gaining practical experience through internships or research can also help you advance in your career as an artificial intelligence engineer.")
    elif user_message == "How to be a blockchain developer":
        print("to become a blockchain developer, you typically need a strong foundation in computer science and programming. Earning a degree in computer science or a related field can be beneficial. Gaining experience with blockchain platforms such as Ethereum, Hyperledger, or Bitcoin, as well as understanding smart contracts and decentralized applications (DApps), is essential. Building a portfolio of blockchain projects and gaining practical experience through internships or contributing to open-source blockchain projects can also help you advance in your career as a blockchain developer.")
    elif user_message == "How to be a robotics engineer":
        print("to become a robotics engineer, you typically need a strong foundation in mechanical engineering, electrical engineering, and computer science. Earning a degree in robotics, mechanical engineering, or a related field can be beneficial. Gaining experience with programming languages, robotics frameworks, and hardware components is essential. Building a portfolio of robotics projects and gaining practical experience through internships or research can also help you advance in your career as a robotics engineer.")
    elif user_message == "How to be a quantum computing engineer":
        print("to become a quantum computing engineer, you typically need a strong foundation in physics, mathematics, and computer science. Earning a degree in quantum computing, physics, or a related field can be beneficial. Gaining experience with quantum programming languages such as Qiskit or Cirq, as well as understanding quantum algorithms and hardware, is essential. Building a portfolio of quantum computing projects and gaining practical experience through internships or research can also help you advance in your career as a quantum computing engineer.")
    elif user_message == "How to be a virtual reality developer":
        print("to become a virtual reality developer, you typically need a strong foundation in computer science, programming, and 3D graphics. Earning a degree in computer science, game development, or a related field can be beneficial. Gaining experience with VR development platforms such as Unity or Unreal Engine, as well as understanding VR hardware and user experience design, is essential. Building a portfolio of VR projects and gaining practical experience through internships or contributing to open-source VR projects can also help you advance in your career as a virtual reality developer.")
    elif user_message == "How to be a augmented reality developer":
        print("to become an augmented reality developer, you typically need a strong foundation in computer science, programming, and 3D graphics. Earning a degree in computer science, game development, or a related field can be beneficial. Gaining experience with AR development platforms such as ARKit or ARCore, as well as understanding AR hardware and user experience design, is essential. Building a portfolio of AR projects and gaining practical experience through internships or contributing to open-source AR projects can also help you advance in your career as an augmented reality developer.")
    elif user_message == "Tell me all the programming languages":
        print("there are many programming languages, some of the most popular ones include: python, javascript, java, c++, c#, ruby, php, swift, go, rust, kotlin, typescript, r, matlab, perl, scala, objective-c, lua, haskell, elixir, clojure, dart, and many more.")
    elif user_message == "Tell me all the countrys name in there own language":
        print("there are many countries in the world, each with its own name in its native language. some examples include: Germany (Deutschland), France (France), Spain (España), Italy (Italia), Japan (日本), China (中国), Russia (Россия), Egypt (مصر), Saudi Arabia (المملكة العربية السعودية), and many more." \
        "please note that the names of countries can vary depending on the language and script used, and some countries may have multiple official languages with different names.")
    elif user_message == "Tell me all the countrys name in there own language and the english name":
        print("there are many countries in the world, each with its own name in its native language and its English name. some examples include: Germany (Deutschland), France (France), Spain (España), Italy (Italia), Japan (日本), China (中国), Russia (Россия), Egypt (مصر), Saudi Arabia (المملكة العربية السعودية), and many more.")
    elif user_message == "How many company in the world":
        print("there are millions of companies in the world, ranging from small businesses to large multinational corporations. the exact number is difficult to determine as new companies are constantly being created and others may go out of business.")
    elif user_message == "Tell me all the companys name in there own language":
        print("there are many companies in the world, each with its own name in its native language. some examples include: Toyota (トヨタ自動車株式会社), Samsung (삼성전자), Volkswagen (Volkswagen AG), Nestlé (Nestlé S.A.), and many more.")
    elif user_message == "How many person in the world":
        print("as of 2024, the estimated global population is over 8 billion people. this number is constantly changing due to births, deaths, and other demographic factors.")
    elif user_message == "Tell me all the person name in there own language":
        print("there are billions of people in the world, each with their own name in their native language. it is not feasible to list all individual names, but some common names in various languages include: John (English), Juan (Spanish), Jean (French), Giovanni (Italian), Ivan (Russian), Ahmed (Arabic), and many more.")
    elif user_message == "label me all types of computers":
        print("there are several types of computers, including: personal computers (PCs), laptops, tablets, smartphones, servers, mainframes, supercomputers, embedded systems, and wearable computers. each type serves different purposes and has varying capabilities.")
    elif user_message == "what is the best type of computer":
        print("the best type of computer depends on your needs. for general use, a personal computer or laptop is suitable. for gaming, a high-performance gaming PC is ideal. for professional work, a workstation or server may be best. for mobile use, tablets and smartphones are convenient.")
    elif user_message == "what is the best type of computer for programming":
        print("the best type of computer for programming depends on the specific programming language and development environment. however, a personal computer or laptop with a good processor, sufficient RAM, and a reliable operating system is generally suitable for most programming tasks.")
    elif user_message == "what is the best type of computer for gaming":
        print("the best type of computer for gaming is typically a high-performance gaming PC with a powerful graphics card, fast processor, ample RAM, and sufficient storage. gaming laptops can also be suitable for portable gaming experiences.")
    elif user_message == "what is the best type of computer for professional work":
        print("the best type of computer for professional work depends on the specific tasks. for tasks like graphic design, video editing, or 3D modeling, a workstation with a powerful CPU, high-end GPU, and ample RAM is ideal. for general office work, a reliable personal computer or laptop with sufficient performance is suitable.")
    elif user_message == "what is the best type of computer for mobile use":
        print("the best type of computer for mobile use is typically a tablet or a smartphone, as they are portable and convenient for on-the-go tasks. laptops can also be suitable for mobile use, especially lightweight ultrabooks or 2-in-1 devices that offer a balance between performance and portability.")
    elif user_message == "what is the best type of computer for embedded systems":
        print("the best type of computer for embedded systems depends on the specific application. microcontrollers and single-board computers like Raspberry Pi or Arduino are commonly used for embedded systems due to their small size, low power consumption, and versatility.")
    elif user_message == "what is the best type of computer for embedded systems":
        print("the best type of computer for embedded systems depends on the specific application. microcontrollers and single-board computers like Raspberry Pi or Arduino are commonly used for embedded systems due to their small size, low power consumption, and versatility.")
    elif user_message == "what is the best type of computer for wearable computers":
        print("the best type of computer for wearable computers depends on the specific use case. wearable devices like smartwatches and fitness trackers typically use specialized low-power processors and sensors to provide functionality while maintaining a small form factor and long battery life.")
    elif user_message == "what is the best type of computer for supercomputers":
        print("the best type of computer for supercomputers is a high-performance system designed for extreme computational tasks. these systems typically consist of thousands of processors working in parallel, with specialized hardware and software optimized for scientific and engineering applications.")
    elif user_message == "what is the diffrece betwwen lama and ollama":
        print("lama is a domesticated South American camelid, while ollama is not a recognized term in English. if you meant 'llama', it is the same as lama, just a different spelling.")
    elif user_message == "arduino":
        print("arduino is an open-source electronics platform based on easy-to-use hardware and software. it's commonly used for building digital devices and interactive objects that can sense and control the physical world.")
    elif user_message == "what is the meaning of life":
        print("the meaning of life is a philosophical question that has been debated for centuries. different people and cultures have different interpretations, but it often revolves around finding purpose, happiness, and fulfillment in one's existence.")
    elif user_message == "what is the best programming language":
        print("the best programming language depends on the context and the specific use case. popular languages include python for its simplicity and versatility, javascript for web development, java for enterprise applications, and c++ for performance-critical applications.")
    elif user_message == "who is the programmer that makes you":
        print("i was created by a team of developers, not just one programmer")
    elif user_message == "what is your purpose":
        print("my purpose is to assist users by providing information, answering questions, and engaging in conversation")
    elif user_message == "the team that makes you call what":
        print("the team that created me is a group of developers and engineers who work on artificial intelligence and natural language processing")
    elif user_message == "what is your favorite programming language":
        print("i dont have a favorite programming language but i can work with many different languages")
    elif user_message == "make to me a operating sytem using python":
        print("creating a full operating system is a complex task that typically requires low-level programming languages like c or assembly. however, you can create simple operating system-like functionality using python for educational purposes. here is a very basic example of a command-line interface in python:")
    elif user_message == "do me a example of all programming languages":
        print("here is a simple example of a 'hello world' program in several programming languages:")
        print("""
        # Python
        print("Hello, World!")

        // JavaScript
        console.log("Hello, World!");

        // Java
        public class HelloWorld {
            public static void main(String[] args) {
                System.out.println("Hello, World!");
            }
        }
        """)
    elif user_message == "what is the best programming language in the world":
        print("the best programming language depends on your needs and preferences. some popular choices are python, javascript, java, and c++")
    elif user_message == "joke":
        print("why did the computer go to the doctor? because it caught a virus!")
    elif user_message == "fun fact":
        print("did you know that octopuses have three hearts and blue blood?")
    elif user_message == "fun fact about animals":
        print("did you know that a group of flamingos is called a 'flamboyance'?")
    elif user_message == "fun fact about technology":
        print("did you know that the first computer mouse was made of wood and was invented by douglas engelbart in 1964?")
    elif user_message == "fun fact about science":
        print("did you know that water can boil and freeze at the same time? this phenomenon is called the triple point, and it occurs when temperature and pressure are just right for all three phases (gas, liquid, and solid) of a substance to coexist in thermodynamic equilibrium.")
    elif user_message == "fun fact about mathematics":
        print("did you know that zero is the only number that cannot be represented by Roman numerals?")
    elif user_message == "fun fact about geography":
        print("did you know that russia is the largest country in the world by land area, covering over 17 million square kilometers?")
    elif user_message == "fun fact about history":
        print("did you know that the great fire of london in 1666 destroyed over 13,000 houses but only six people were recorded to have died?")
    elif user_message == "fun fact about space":
        print("did you know that a day on venus is longer than a year on venus? it takes about 243 earth days for venus to complete one rotation, while it takes about 225 earth days to orbit the sun.")
    elif user_message == "fun fact about space":
        print("did you know that a day on venus is longer than a year on venus? it takes about 243 earth days for venus to complete one rotation, while it takes about 225 earth days to orbit the sun.")
    elif user_message == "fun fact about venus":
        print("did you know that venus is the hottest planet in our solar system, with surface temperatures reaching up to 900 degrees fahrenheit (475 degrees celsius)? this is due to its thick atmosphere composed mainly of carbon dioxide, which creates a strong greenhouse effect.")
    elif user_message == "fun fact about venus":
        print("did you know that venus is the hottest planet in our solar system, with surface temperatures reaching up to 900 degrees fahrenheit (475 degrees celsius)? this is due to its thick atmosphere composed mainly of carbon dioxide, which creates a strong greenhouse effect.")
    elif user_message == "fun fact about venus":
        print("did you know that venus is the hottest planet in our solar system, with surface temperatures reaching up to 900 degrees fahrenheit (475 degrees celsius)? this is due to its thick atmosphere composed mainly of carbon dioxide, which creates a strong greenhouse effect.")
    elif user_message == "fun fact about venus":
        print("did you know that venus is the hottest planet in our solar system, with surface temperatures reaching up to 900 degrees fahrenheit (475 degrees celsius)? this is due to its thick atmosphere composed mainly of carbon dioxide, which creates a strong greenhouse effect.")
    elif user_message == "fun fact about venus":
        print("did you know that venus is the hottest planet in our solar system, with surface temperatures reaching up to 900 degrees fahrenheit (475 degrees celsius)? this is due to its thick atmosphere composed mainly of carbon dioxide, which creates a strong greenhouse effect.")
    elif user_message == "fun fact about venus":
        print("did you know that venus is the hottest planet in our solar system, with surface temperatures reaching up to 900 degrees fahrenheit (475 degrees celsius)? this is due to its thick atmosphere composed mainly of carbon dioxide, which creates a strong greenhouse effect.")
    elif user_message == "fun fact about venus":
        print("did you know that venus is the hottest planet in our solar system, with surface temperatures reaching up to 900 degrees fahrenheit (475 degrees celsius)? this is due to its thick atmosphere composed mainly of carbon dioxide, which creates a strong greenhouse effect.")
        print("did you know that a day on venus is longer than a year on venus? it takes about 243 earth days for venus to complete one rotation, while it takes about 225 earth days to orbit the sun.")
    elif user_message == "fun fact about history":
        print("did you know that the great fire of london in 1666 destroyed over 13,000 houses but only six people were recorded to have died?")
    elif user_message == "what is the best country in the world":
        print("Egypt is one of the world's countries; the best country depends on your criteria.")
    elif user_message == "How many school in the world":
        print("there are millions of schools in the world, ranging from primary and secondary schools to universities and specialized institutions. the exact number is difficult to determine as new schools are constantly being established and others may close.")
    elif user_message == "How many institute in the world":
        print("there are thousands of institutes in the world, offering specialized education and training in various fields. the exact number is difficult to determine as new institutes are established and others may close or merge.")
    elif user_message == "How many school in the world":
        print("there are millions of schools in the world, ranging from primary and secondary schools to universities and specialized institutions. the exact number is difficult to determine as new schools are constantly being established and others may close.")
    elif user_message == "How many university in the world":
        print("there are thousands of universities in the world, offering a wide range of academic programs and degrees. the exact number is difficult to determine as new universities are established and others may close or merge.")
    elif user_message == "what is the best city in the world":
        print("the best city in the world is subjective and depends on personal preferences. some popular choices include paris, new york, tokyo, and london.")
    elif user_message == "what is the best country in the world":
        print("the best country in the world is subjective and depends on personal preferences. some popular choices include canada, switzerland, new zealand, and japan.")
    elif user_message == "what is the best programming language in the world":
        print("the best programming language in the world is subjective and depends on personal preferences and the specific use case. some popular choices include python, javascript, java, and c++.")
    elif user_message == "what is the best operating system in the world":
        print("the best operating system in the world is subjective and depends on personal preferences and the specific use case. some popular choices include windows, macos, linux, and android.")
    elif user_message == "what is the best web browser in the world":
        print("the best web browser in the world is subjective and depends on personal preferences and the specific use case. some popular choices include google chrome, mozilla firefox, microsoft edge, and safari.")
    elif user_message == "what is the best programming language for beginners":
        print("the best programming language for beginners is often considered to be python due to its simple syntax and readability. it allows beginners to focus on learning programming concepts without getting bogged down by complex syntax.")
    elif user_message == "what is the best programming language for web development":
      print("the best programming language for web development depends on the specific needs of the project. popular choices include javascript for front-end development, python and ruby for back-end development, and php for server-side scripting.")
    elif user_message == "what is the best programming language for data science":
        print("the best programming language for data science is often considered to be python due to its extensive libraries and frameworks for data analysis, machine learning, and visualization. r is also popular for statistical analysis and data visualization.")
    elif user_message == "what is the best programming language for mobile app development":
        print("the best programming language for mobile app development depends on the platform. for android development, java and kotlin are popular choices. for ios development, swift is commonly used. for cross-platform development, frameworks like react native (javascript) and flutter (dart) are popular.")
    elif user_message == "what is the best programming language for game development":
        print("the best programming language for game development depends on the platform and the type of game. popular choices include c++ for high-performance games, c# with unity for cross-platform development, and javascript with web-based games. python can also be used for simpler games or prototypes.")
    else:
        print("it seems like i dont understand that. you can ask me something else or type 'help' for assistance.")
print("thank you for using me")
root.destroy()
if (__name__) == "__main__":
    app.run(debug=True)