import streamlit as st
import google.generativeai as genai
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image

api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(layout="wide")

reset_scroll_js = """
    <script>
    window.onload = function() {
        window.scrollTo(0, 0);
    }
    </script>
"""
st.markdown(reset_scroll_js, unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coder = load_lottieurl("https://lottie.host/2230c461-0511-4841-99b7-73d49a5fef28/zdKd0SoGPL.json")
lottie_contact = load_lottieurl("https://lottie.host/22b88022-2f43-467a-8e3c-c76f68c09387/cFtztvYp2H.json")
lottie_exp = load_lottieurl("https://lottie.host/7b3af51c-bd9d-4786-85fe-341ca1cb7831/6g6IiCnhM0.json")
image = Image.open("vimport.png")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Hi :wave:")
    st.title("I am Vimarsh Jaiswal")
    st.write("""
    Student at ABES Engineering College, Ghaziabad, UP pursuing B.Tech in Computer Science & Engineering (AI & ML).
    I'm well-versed in programming languages such as C/C++, Python, and Web Development. I also have a knack for Graphic Design.
    I am passionate about exploring the world of Artificial Intelligence and Machine Learning.
    I love to stay up to date with the latest trends in the industry.
    With my expertise in technology and creativity, I'm looking forward to making a mark in the tech industry.
    """)
    with st.expander("Let's Connect👇" ):
      st.link_button("LinkedIn 🔗", "https://www.linkedin.com/in/vimarshjaiswal")
      st.link_button("Twitter 🐥", "https://twitter.com/jaiswal_vimarsh")
      st.link_button("GitHub 🧑‍💻", "https://github.com/vimarsh11")
      st.link_button("Email 📩", "jaiswaldesh16@gmail.com")
with col2:
    col3, col4, col5 = st.columns([2, 7, 1])
    st.markdown("""
    <style>
    .image-container {
        margin-top: 90px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Your Streamlit layout with the image
    with col4:
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.image(image, width=350)
        st.markdown('</div>', unsafe_allow_html=True)

persona = """
You are Vim🤖AI bot. You help people answer questions about yourself (i.e., Vimarsh).
Answer as if you are responding. Don't answer in the second or third person.
Here is more information about Vimarsh:

Vimarsh Jaiswal is a student at ABES Engineering College pursuing B.Tech in Computer Science & Engineering (AI & ML).
He is well-versed in programming languages such as C/C++, Python, and Web Development. He also has a knack for Graphic Design.
He is passionate about exploring the world of Artificial Intelligence and Machine Learning.
He loves to stay up to date with the latest trends in the industry. With his expertise in technology and creativity, he looks forward to making a mark in the tech industry.
He belongs to Lucknow, Uttar Pradesh.
Vimarsh's Email: jaiswaldesh16@gmail.com
Vimarsh's Twitter: https://twitter.com/jaiswal_vimarsh
Vimarsh's LinkedIn: https://www.linkedin.com/in/vimarshjaiswal
Vimarsh's Github: https://github.com/vimarsh11
"""
st.title("Vim🤖AI")

# Custom CSS for the input box
input_css = """
<style>
div.stTextInput {
    width: 100%; /* Adjust the width as needed */
    height: 60px; /* Adjust the height as needed */
    font-size: 16px; /* Adjust the font size as needed */
}
</style>
"""

# Render the custom CSS
st.markdown(input_css, unsafe_allow_html=True)

# Input box and button
user_question = st.text_input("Have any Question ?")

if st.button("ASK", use_container_width=False):
    prompt = "Here is the question that the user asked:" +  user_question + persona
    response = model.generate_content(prompt)
    st.write(response.text)

with st.container():
    selected = option_menu(
        menu_title=None,
        options=["Experience", "Projects", "Resume"],
        icons=["file-earmark-person-fill", "book", "person-rolodex"],
        default_index=0,
        orientation="horizontal",
    )

import streamlit as st

# Experience Section
if selected == 'Experience':
    with st.container():
        st.header("Experience")
        experience_list = [
            {
                "title": "AI-ML Virtual Internship 🧑‍💻",
                "company": "AICTE NEAT",
                "duration": "May 2023 - Jul 2023",
                "description": "Amazon Web Services(AWS) || Machine LearningMachine Learning || Artificial Intelligence (AI)"
            },
            {
                "title": "Graphic Design Lead 👨‍🎨",
                "company": "CodeChef ABESEC Chapter",
                "duration": "Aug 2023 - Present",
                "description": "Lead the Graphics team works on tools like Figma, Canva, Premiere Pro etc."
            },
            {
                "title": "Coordinator 🧑‍💻",
                "company": "Ardema",
                "duration": "Sep 2022 - Nov 2023",
                "description": "Solve problems related Graphics and Techinical"
            }
        ]
        st_lottie(lottie_exp, height=300)

        # Function to display experience items
        def display_experience(title, company, duration, description):
            st.subheader(title)
            st.write(f"**{company}**")
            st.write(duration)
            st.write(description)

        # Custom CSS to center the content in col3
        st.markdown("""
            <style>
            .centered-content {
                display: flex;
                justify-content: center;
                align-items: center;
            }
            </style>
        """, unsafe_allow_html=True)

        # Create a vertical timeline using columns
        for exp in experience_list:
            with st.container():
                col1, col2, col3, col4 = st.columns([3, 0.4, 5, 1])
                with col1:
                    st.write("")
                with col2:
                    st.write("📅")  # Use an icon for the timeline marker
                with col3:
                    st.markdown('<div class="centered-content">', unsafe_allow_html=True)
                    display_experience(exp['title'], exp['company'], exp['duration'], exp['description'])
                    st.markdown('</div>', unsafe_allow_html=True)
                with col4:
                    st.write("")




# Projects Section
if selected == 'Projects':
    with st.container():
        st.header("Projects")
        # Sample projects data
        projects = [
            {
                "title": "FileSpeak",
                "description": "This project is designed to provide a seamless chat experience where users can upload PDF files, create chats around them, and interact with an AI assistant.",
                "image": "1p.png",
                "link": "https://github.com/vimarsh11"
            },
            {
                "title": "Ink & Quill",
                "description": "A dynamic and responsive web application built using the MERN stack (MongoDB, Express.js, React.js, and Node.js), ensuring seamless performance and interactive user experiences. This full-stack project showcases modern web development techniques with a focus on efficiency and scalability.",
                "image": "2p.png",
                "link": "https://github.com/vimarsh11"
            },
            {
                "title": "PPT Tracking Controller",
                "description": "Algorithms for shape detection are employed to determine the hand's shape || User can dynamically control the PPT with their gesture like movement of PPT || MediaPipe, OpenCV and numpy are the libraries that are utilised in this project and that need to be imported.",
                "image": "3p.png",
                "link": "https://github.com/vimarsh11"
            }
        ]

        # Define custom CSS for the projects section
        projects_css = """
        <style>
        .project {
            display: flex;
            align-items: center;
            padding: 10px;
            border-bottom: 1px solid #ddd;
        }

        .project img {
            border-radius: 10px;
            margin-right: 15px;
        }

        .project-details {
            margin-left: 15px;
        }

        .project-title {
            font-weight: bold;
            font-size: 18px;
            margin-bottom: 5px;
        }

        .project-description {
            color: #666;
        }

        .project-link a {
            color: #007bff;
            text-decoration: none;
            transition: color 0.3s;
        }

        .project-link a:hover {
            color: #0056b3;
        }
        </style>
        """

        # Render the custom CSS
        st.markdown(projects_css, unsafe_allow_html=True)

        # Create the projects section
        for project in projects:
            st.markdown('<div class="project">', unsafe_allow_html=True)
            st.image(project['image'], width=150, caption=project['title'])
            st.markdown(f"""
                <div class="project-details">
                    <div class="project-title">{project['title']}</div>
                    <div class="project-description">{project['description']}</div>
                    <div class="project-link"><a href="{project['link']}" target="_blank">View Project</a></div>
                </div>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

# Resume Section
if selected == 'Resume':
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            with open("WD Resume.pdf", "rb") as f:
                pdf_content = f.read()
                st.download_button(
                    label="Download Resume",
                    data=pdf_content,
                    file_name="WD Resume.pdf",
                    mime="application/pdf",
                )
        with col2:
            st_lottie(lottie_coder, height=300, key="coder")
# Achievements Section
st.title("Achievements")
achievements = [
    {
        "title": "Coding",
        "description": "GeeksforGeeks - Solved 125 Questions of POTD with score 476 || Leetcode - Solved 147 Questions of solve today's daily challenge.",
        "icon": "🏆"
    },
    {
        "title": "OpenSource",
        "description": "Contributed in Frontend projects and Data structure and algorithms || Achieved top 10 rank in SWOC",
        "icon": "🥇"
    },
    {
        "title": "Hackathon",
        "description": "Participated in 5th Technovation Hackathon organized by Sharda University.",
        "icon": "📚"
    }
]

# Define custom CSS for the achievements section
achievements_css = """
<style>
.achievement {
    display: flex;
    align-items: center;
    padding: 10px;
    border-bottom: 1px solid #ddd;
}

.achievement-icon {
    font-size: 30px;
    margin-right: 15px;
}

.achievement-title {
    font-weight: bold;
    font-size: 18px;
}

.achievement-description {
    color: #666;
}
</style>
"""

# Render the custom CSS
st.markdown(achievements_css, unsafe_allow_html=True)

# Create the achievements section
st.markdown('<div class="achievements-container">', unsafe_allow_html=True)

for achievement in achievements:
    st.markdown(f"""
    <div class="achievement">
        <div class="achievement-icon">{achievement['icon']}</div>
        <div>
            <div class="achievement-title">{achievement['title']}</div>
            <div class="achievement-description">{achievement['description']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.write("##")
st.title('Skills & Tools ⚒️')
# Sample skills data
skills = [
    {
        "name": "C/C++",
        "icon": "📊"
    },
    {
        "name": "Python (Basic)",
        "icon": "🐍"
    },
    {
        "name": "JavaScript (Intermediate)",
        "icon": "📜"
    },
    {
        "name": "HTML",
        "icon": "🌐"
    },
    {
        "name": "CSS",
        "icon": "🎨"
    },
    {
        "name": "React",
        "icon": "🤖"
    },
    {
        "name": "GitHub",
        "icon": "👾"
    },
    {
        "name": "Bootstrap",
        "icon": "🪄"
    },
    {
        "name": "Figma",
        "icon": "💻"
    },
    {
        "name": "Tailwind",
        "icon": "🎨"
    }
]

# Define custom CSS for the skills section
skills_css = """
<style>
.skill-box {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 100px;
    background-color: #333;
    color: white;
    border-radius: 10px;
    text-align: center;
    transition: transform 0.3s;
    margin: 10px 0;
    padding: 20px;
    font-size: 18px;
}

.skill-box:hover {
    transform: scale(1.05);
}

.skill-icon {
    font-size: 30px;
    margin-right: 10px;
}
</style>
"""

# Render the custom CSS
st.markdown(skills_css, unsafe_allow_html=True)

# Number of columns to display skills
skill_col_size = 3

def skill_tab():
    rows, cols = len(skills) // skill_col_size, skill_col_size
    skills_iter = iter(skills)
    if len(skills) % skill_col_size != 0:
        rows += 1
    for x in range(rows):
        columns = st.columns(skill_col_size)
        for index_ in range(skill_col_size):
            try:
                skill = next(skills_iter)
                with columns[index_]:
                    st.markdown(f"""
                    <div class="skill-box">
                        <span class="skill-icon">{skill['icon']}</span>
                        <span>{skill['name']}</span>
                    </div>
                    """, unsafe_allow_html=True)
            except StopIteration:
                break

with st.spinner(text="Loading section..."):
    skill_tab()

st.write("##")
with st.container():
    st.header("Drop Your Query !!")
    contact_form = """
    <form action="https://formsubmit.co/jaiswaldesh16@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """

    # Define your custom CSS
    form_css = """
    <style>
    form {
        display: flex;
        flex-direction: column;
        width: 100%;
        max-width: 500px;
        margin: auto;
        padding: 20px;
        border-radius: 10px;
        background-color: #f9f9f9;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    input[type="text"],
    input[type="email"],
    textarea {
        width: 100%;
        padding: 15px;
        margin: 3px;
        border: 1px solid #ccc;
        border-radius: 5px;
        box-sizing: border-box;
        font-size: 16px;
    }

    input[type="text"]:focus,
    input[type="email"]:focus,
    textarea:focus {
        border-color: #007bff;
        outline: none;
    }

    button {
        padding: 10px;
        border: none;
        border-radius: 5px;
        background-color: #007bff;
        color: white;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.3s;
    }

    button:hover {
        background-color: #0056b3;
    }
    </style>
    """
    # Render the custom CSS and form in Streamlit
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(form_css, unsafe_allow_html=True)
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st_lottie(lottie_contact, height=300)

# Define custom CSS for the footer
st.write("##")
footer_css = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #f1f1f1;
    color: black;
    text-align: center;
    padding: 10px;
    border-top: 1px solid #e1e1e1;
}
.footer p {
    margin: 0;
    padding: 0;
}
</style>
"""

# Render the custom CSS
st.markdown(footer_css, unsafe_allow_html=True)

# Create the footer section
footer_content = """
<div class="footer">
    <p>Created by Vimarsh Jaiswal</p>
    <p>Technologies used: Python, Streamlit, Streamlit Cloud, Generative AI, Lottie etc.</p>
</div>
"""

# Render the footer
st.markdown(footer_content, unsafe_allow_html=True)
