import streamlit as st

def main():
    st.title("Welcome to Rofoo's Hiring Portal")
    st.subheader("Be Part of a Revolutionary Startup")

    st.markdown(
        """
        Rofoo is an innovative startup revolutionizing the restaurant industry through AI-powered humanoid solutions. While these initial roles are unpaid, they offer an unparalleled opportunity to contribute to cutting-edge technology and gain invaluable experience in an entrepreneurial environment. 
        
        **Commitment:** 10-20 hours per week.
        """
    )

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

    if selected_role == "AI Engineer":
        display_ai_engineer()
    elif selected_role == "Computer Vision Engineer":
        display_cv_engineer()
    elif selected_role == "Design Engineer":
        display_design_engineer()
    elif selected_role == "Mechanical Engineer":
        display_mechanical_engineer()
    elif selected_role == "Marketing Associate":
        display_marketing_associate()
    elif selected_role == "Robotics Engineer":
        display_robotics_engineer()

    st.markdown("---")
    st.markdown(
        """
        ### Ready to Join Us?
        Click the button below to apply now!
        """
    )
    st.markdown("[Apply Now](https://forms.gle/hJVMaHSzQLSZXSkQ7) ", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(
        """
        ### Letters of Recommendation
        At Rofoo, we value the trust and credibility that a letter of recommendation can bring to your application. If selected, Rofoo will provide a personalized Letter of Recommendation upon successful completion of your tenure, highlighting your contributions and achievements. This letter can be a valuable addition to your professional portfolio, supporting your career growth in the tech industry.

        Join us and let your work speak volumes!
        """
    )

def display_ai_engineer():
    st.header("AI Engineer")
    st.markdown(
        """
        **Role Overview:**
        As an AI Engineer at Rofoo, you will work on developing and fine-tuning AI algorithms that drive our humanoid’s intelligence and interaction capabilities.

        **Key Responsibilities:**
        - Develop and optimize machine learning models for NLP and reinforcement learning.
        - Integrate AI algorithms with hardware systems to enable real-time decision-making.
        - Collaborate with a multidisciplinary team to align AI features with product objectives.

        **Skills Required:**
        - Proficiency in Python, TensorFlow, or PyTorch.
        - Expertise in natural language processing and reinforcement learning.
        - Experience in integrating AI with robotics hardware.
        - Strong problem-solving and analytical skills.

        **What You Gain:**
        - Hands-on experience with advanced AI technologies.
        - Exposure to real-world challenges in robotics and service automation.
        - Opportunity to build impactful AI solutions for the restaurant industry.
        """
    )

def display_cv_engineer():
    st.header("Computer Vision Engineer")
    st.markdown(
        """
        **Role Overview:**
        As a Computer Vision Engineer, you will develop cutting-edge vision systems that empower Rofoo to navigate environments, recognize objects, and interact seamlessly with its surroundings.

        **Key Responsibilities:**
        - Design and implement algorithms for object detection, tracking, and pathfinding.
        - Develop real-time image processing systems using CNNs and vision-based sensors.
        - Collaborate with robotics and AI teams to optimize vision functionality.

        **Skills Required:**
        - Proficiency in OpenCV, PyTorch, and TensorFlow.
        - Expertise in convolutional neural networks and image processing.
        - Experience with real-time video analysis and object tracking.
        - Familiarity with SLAM (Simultaneous Localization and Mapping).

        **What You Gain:**
        - Experience in designing and deploying computer vision systems in robotics.
        - Work with state-of-the-art tools like OpenCV, PyTorch, and TensorFlow.
        - A chance to contribute to groundbreaking technology in a startup environment.
        """
    )

def display_design_engineer():
    st.header("Design Engineer")
    st.markdown(
        """
        **Role Overview:**
        As a Design Engineer, you will be responsible for conceptualizing and developing Rofoo’s structure and appearance, ensuring it aligns with operational requirements and brand identity.

        **Key Responsibilities:**
        - Create detailed CAD models and prototypes for Rofoo’s physical design.
        - Ensure designs meet ergonomic and safety standards for human-robot interaction.
        - Collaborate with mechanical engineers to refine prototypes for manufacturing.

        **Skills Required:**
        - Proficiency in CAD software like SolidWorks, AutoCAD, or Fusion 360.
        - Understanding of material properties and manufacturing processes.
        - Strong visualization and creative problem-solving skills.
        - Experience with rapid prototyping and iterative design.

        **What You Gain:**
        - Practical experience in designing consumer-facing robotics.
        - Hands-on exposure to the design-to-prototype pipeline.
        - A portfolio piece showcasing your work on a pioneering AI humanoid.
        """
    )

def display_mechanical_engineer():
    st.header("Mechanical Engineer")
    st.markdown(
        """
        **Role Overview:**
        As a Mechanical Engineer, you will design and optimize Rofoo’s mechanical systems to ensure reliability and performance in real-world environments.

        **Key Responsibilities:**
        - Develop and test mechanical components like actuators and joints.
        - Conduct stress and durability analysis to ensure system reliability.
        - Collaborate with design and robotics teams to ensure seamless integration.

        **Skills Required:**
        - Proficiency in mechanical design tools like SolidWorks and MATLAB.
        - Knowledge of robotics kinematics and dynamics.
        - Experience with finite element analysis (FEA) and prototyping.
        - Strong understanding of material science and mechanical systems.

        **What You Gain:**
        - Practical experience in robotics and mechanical engineering.
        - An opportunity to see your designs come to life in a functional humanoid.
        - Valuable insights into the hardware aspects of AI-driven solutions.
        """
    )

def display_marketing_associate():
    st.header("Marketing Associate")
    st.markdown(
        """
        **Role Overview:**
        As a Marketing Associate, you will develop and execute strategies to promote Rofoo, build its brand, and attract potential clients and investors.

        **Key Responsibilities:**
        - Design marketing campaigns highlighting Rofoo’s features and benefits.
        - Create engaging content for social media, websites, and promotional materials.
        - Conduct market research to identify trends and target audiences.

        **Skills Required:**
        - Strong written and verbal communication skills.
        - Proficiency in digital marketing tools and platforms like Google Ads and social media analytics.
        - Creativity in designing marketing campaigns and content.
        - Analytical mindset to evaluate campaign performance.

        **What You Gain:**
        - Real-world experience in marketing and brand-building for a tech startup.
        - Opportunity to work closely with a founding team, shaping the company’s image.
        - A chance to showcase your creativity in campaigns with tangible results.
        """
    )

def display_robotics_engineer():
    st.header("Robotics Engineer")
    st.markdown(
        """
        **Role Overview:**
        As a Robotics Engineer, you will develop and maintain Rofoo’s robotic systems, ensuring precision and reliability in its operations.

        **Key Responsibilities:**
        - Design and implement motion planning, navigation, and task execution algorithms.
        - Integrate sensors like LIDAR and ultrasonic modules for safe navigation.
        - Optimize robotics systems for performance and user interaction.

        **Skills Required:**
        - Proficiency in programming languages like Python, C++, and ROS.
        - Expertise in motion planning and control systems.
        - Experience with sensor integration and feedback control.
        - Familiarity with robotics simulation tools like Gazebo or V-REP.

        **What You Gain:**
        - Hands-on experience in robotics system development and integration.
        - Collaboration with AI and vision experts to create an advanced humanoid.
        - Exposure to the entrepreneurial process of building robotics for real-world applications.
        """
    )

if __name__ == "__main__":
    main()
