import streamlit as st

def main():
    # Hide Streamlit default menu and footer
    hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    # Title and introduction
    st.title("Welcome to Rofoo's Hiring Portal")
    st.subheader("Be Part of a Revolutionary Startup")

    st.markdown(
        """
        Rofoo is an innovative startup revolutionizing the restaurant industry through AI-powered humanoid solutions. 
        While these initial roles are unpaid, they offer an unparalleled opportunity to contribute to cutting-edge 
        technology and gain invaluable experience in an entrepreneurial environment.

        **Commitment:** 10-20 hours per week.
        """
    )

    # Sidebar for roles
    st.sidebar.title("Explore Roles")
    roles = [
        "AI Engineer",
        "Computer Vision Engineer",
        "Design Engineer",
        "Mechanical Engineer",
        "Marketing Associate",
        "Robotics Engineer",
    ]
    selected_role = st.sidebar.selectbox("Select a Role", roles)

    # Display selected role details
    if selected_role == "AI Engineer":
        display_role(
            "AI Engineer",
            """
            **Role Overview:**
            As an AI Engineer at Rofoo, you will work on developing and fine-tuning AI algorithms that drive our humanoid’s intelligence and interaction capabilities.

            **Key Responsibilities:**
            - Develop and optimize machine learning models for NLP and reinforcement learning.
            - Integrate AI algorithms with hardware systems to enable real-time decision-making.
            - Collaborate with a multidisciplinary team to align AI features with product objectives.

            **What You Gain:**
            - Hands-on experience with advanced AI technologies.
            - Exposure to real-world challenges in robotics and service automation.
            - Opportunity to build impactful AI solutions for the restaurant industry.
            """
        )
    elif selected_role == "Computer Vision Engineer":
        display_role(
            "Computer Vision Engineer",
            """
            **Role Overview:**
            As a Computer Vision Engineer, you will develop cutting-edge vision systems that empower Rofoo to navigate environments, recognize objects, and interact seamlessly with its surroundings.

            **Key Responsibilities:**
            - Design and implement algorithms for object detection, tracking, and pathfinding.
            - Develop real-time image processing systems using CNNs and vision-based sensors.
            - Collaborate with robotics and AI teams to optimize vision functionality.

            **What You Gain:**
            - Experience in designing and deploying computer vision systems in robotics.
            - Work with state-of-the-art tools like OpenCV, PyTorch, and TensorFlow.
            - A chance to contribute to groundbreaking technology in a startup environment.
            """
        )
    elif selected_role == "Design Engineer":
        display_role(
            "Design Engineer",
            """
            **Role Overview:**
            As a Design Engineer, you will be responsible for conceptualizing and developing Rofoo’s structure and appearance, ensuring it aligns with operational requirements and brand identity.

            **Key Responsibilities:**
            - Create detailed CAD models and prototypes for Rofoo’s physical design.
            - Ensure designs meet ergonomic and safety standards for human-robot interaction.
            - Collaborate with mechanical engineers to refine prototypes for manufacturing.

            **What You Gain:**
            - Practical experience in designing consumer-facing robotics.
            - Hands-on exposure to the design-to-prototype pipeline.
            - A portfolio piece showcasing your work on a pioneering AI humanoid.
            """
        )
    elif selected_role == "Mechanical Engineer":
        display_role(
            "Mechanical Engineer",
            """
            **Role Overview:**
            As a Mechanical Engineer, you will design and optimize Rofoo’s mechanical systems to ensure reliability and performance in real-world environments.

            **Key Responsibilities:**
            - Develop and test mechanical components like actuators and joints.
            - Conduct stress and durability analysis to ensure system reliability.
            - Collaborate with design and robotics teams to ensure seamless integration.

            **What You Gain:**
            - Practical experience in robotics and mechanical engineering.
            - An opportunity to see your designs come to life in a functional humanoid.
            - Valuable insights into the hardware aspects of AI-driven solutions.
            """
        )
    elif selected_role == "Marketing Associate":
        display_role(
            "Marketing Associate",
            """
            **Role Overview:**
            As a Marketing Associate, you will develop and execute strategies to promote Rofoo, build its brand, and attract potential clients and investors.

            **Key Responsibilities:**
            - Design marketing campaigns highlighting Rofoo’s features and benefits.
            - Create engaging content for social media, websites, and promotional materials.
            - Conduct market research to identify trends and target audiences.

            **What You Gain:**
            - Real-world experience in marketing and brand-building for a tech startup.
            - Opportunity to work closely with a founding team, shaping the company’s image.
            - A chance to showcase your creativity in campaigns with tangible results.
            """
        )
    elif selected_role == "Robotics Engineer":
        display_role(
            "Robotics Engineer",
            """
            **Role Overview:**
            As a Robotics Engineer, you will develop and maintain Rofoo’s robotic systems, ensuring precision and reliability in its operations.

            **Key Responsibilities:**
            - Design and implement motion planning, navigation, and task execution algorithms.
            - Integrate sensors like LIDAR and ultrasonic modules for safe navigation.
            - Optimize robotics systems for performance and user interaction.

            **What You Gain:**
            - Hands-on experience in robotics system development and integration.
            - Collaboration with AI and vision experts to create an advanced humanoid.
            - Exposure to the entrepreneurial process of building robotics for real-world applications.
            """
        )

    # Application section
    st.markdown("---")
    st.markdown(
        """
        ### Ready to Join Us?
        Click the button below to apply now!
        """
    )
    st.markdown("[Apply Now](https://forms.gle/hJVMaHSzQLSZXSkQ7)", unsafe_allow_html=True)


def display_role(title, content):
    st.header(title)
    st.markdown(content)


if __name__ == "__main__":
    main()
