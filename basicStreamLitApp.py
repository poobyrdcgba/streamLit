import streamlit as st
from PIL import Image

st.set_page_config(page_title="Portfolio of Robert David Cala", layout="centered")

st.title("Portfolio of Robert David Cala")

profile_image = Image.open("assets/profile.jpg")

if 'show_image' not in st.session_state:
    st.session_state.show_image = False

def toggle_image():
    st.session_state.show_image = not st.session_state.show_image

button_text = "Click to see a handsome guy" if not st.session_state.show_image else "Hide"
if st.button(button_text):
    toggle_image()

if st.session_state.show_image:
    st.image(profile_image, width=200, caption="Robert David Cala")

st.header("Biography")
st.write("""
My name is Robert David Cala, and I was born in Leyte, a province known for its rich history and beautiful landscapes. Though I was born in Leyte, my formative years were spent in Negros Oriental, where I attended Pacuan National High School. It was there that I developed a keen interest in technology and began to envision a future in the world of IT.

Currently, I am a third-year student at Cebu Institute of Technology - University, where I am pursuing a Bachelor of Science in Information Technology (BSIT). As a working student, I have learned to juggle academic commitments with work responsibilities, a challenging but rewarding experience that has shaped me into a more disciplined and resilient individual.

Outside of my studies, I enjoy playing chess and basketball. These hobbies have not only provided me with relaxation and fun but have also helped me hone valuable skills like strategic thinking, teamwork, and perseverance—qualities that are essential both on the court and in life.

Looking forward, my goal is to become a proficient developer, specializing in creating innovative websites and engaging games. I am passionate about the potential of technology to solve problems, create new experiences, and bring people together. I am eager to continue learning and growing, and I am excited to see where this journey will take me.

As I look to the future, I am committed to making a positive impact in the tech world, always driven by curiosity, creativity, and a desire to learn.
""")

st.header("Education")
st.write("""
- **High School**: Pacuan National High School, Negros Oriental
- **Current Studies**: Bachelor of Science in Information Technology (BSIT), Cebu Institute of Technology - University (3rd Year)
""")

st.header("Career")
st.write("""
Currently, I am focused on my studies and gaining valuable experience as a working student at Cebu Institute of Technology - University. My journey as a working student has helped me develop strong time management skills and a resilient work ethic.
""")

st.header("Personal Achievements")
st.write("""
- **Chess**: I enjoy playing chess, which helps me develop strategic thinking and problem-solving skills.
- **Basketball**: Playing basketball has taught me teamwork and perseverance.
""")

st.header("Future Goals")
st.write("""
My goal is to become a proficient developer, specializing in creating innovative websites and engaging games. I am passionate about using technology to solve problems and bring joy to others, and I am eager to continue learning and growing in this ever-evolving field.
""")

st.header("Projects")
st.write("Here are some of my notable projects:")

st.subheader("1. Personal Website")
st.write("""
- **Description**: A personal website created to showcase my skills, projects, and contact information.
- **Technologies Used**: HTML, CSS, JavaScript
- **GitHub Account**: [https://github.com/poobyrdcgba](https://github.com/poobyrdcgba)
""")

st.header("Contact")
st.write("""
Feel free to reach out to me via [09631668797](tel:09631668797) or email me at [robertdavid.cala@cit.edu](mailto:robertdavid.cala@cit.edu) for any inquiries or collaboration opportunities!
""")

video_file = open("assets/myvideo.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)

st.markdown("---")
st.write("© 2024 Robert David Cala. All Rights Reserved.")
