import streamlit as st

# Page config
st.set_page_config(page_title="AI Workshop Sandbox", layout="wide")

# Initialize session state
if 'responses' not in st.session_state:
    st.session_state.responses = {'noAI': '', 'withAI': '', 'withFramework': ''}
if 'task_input' not in st.session_state:
    st.session_state.task_input = ''
if 'current_group' not in st.session_state:
    st.session_state.current_group = None

# Header
st.title("Phase 2: Interactive AI Sandbox")
st.markdown("""
Split into three groups and complete the same task using different approaches. 
**Each group should time themselves** to compare efficiency.
""")

st.info("Facilitator: Start timing each group when they begin!")

# Task Input Section
st.header("Workshop Task")
st.write("Facilitator: Enter the task all groups will complete")
task_input = st.text_area(
    "Task Description",
    value=st.session_state.task_input,
    placeholder="Example: Write a professional email declining a meeting invitation while suggesting alternative times...",
    height=100,
    key="task_area"
)
st.session_state.task_input = task_input

st.divider()

# Group Selection
st.header("Select Your Group")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Group 1: No AI", use_container_width=True, type="primary" if st.session_state.current_group == 'noAI' else "secondary"):
        st.session_state.current_group = 'noAI'
    st.caption("Complete the task without any AI assistance")

with col2:
    if st.button("Group 2: With AI", use_container_width=True, type="primary" if st.session_state.current_group == 'withAI' else "secondary"):
        st.session_state.current_group = 'withAI'
    st.caption("Use AI to help complete the task")

with col3:
    if st.button("Group 3: AI + Framework", use_container_width=True, type="primary" if st.session_state.current_group == 'withFramework' else "secondary"):
        st.session_state.current_group = 'withFramework'
    st.caption("Use AI with our prompting framework")

st.divider()

# Framework Display for Group 3
if st.session_state.current_group == 'withFramework':
    st.header("Effective Prompting Framework")
    
    framework_steps = [
        ("Context", "Provide background information and relevant details"),
        ("Task", "Clearly state what you want the AI to do"),
        ("Format", "Specify the desired output format"),
        ("Constraints", "Set any limitations or requirements"),
        ("Examples", "Include examples if helpful")
    ]
    
    for i, (label, description) in enumerate(framework_steps, 1):
        with st.container():
            col_num, col_content = st.columns([1, 9])
            with col_num:
                st.markdown(f"**{i}**")
            with col_content:
                st.markdown(f"**{label}**: {description}")
    
    st.divider()

# Work Area
if st.session_state.current_group:
    group_names = {
        'noAI': 'Group 1: No AI',
        'withAI': 'Group 2: With AI',
        'withFramework': 'Group 3: AI + Framework'
    }
    
    group_instructions = {
        'noAI': 'Work together as a team to solve the problem using traditional methods.',
        'withAI': 'Use an AI tool with your own prompts to solve the problem.',
        'withFramework': 'Apply the framework above to structure your AI prompts.'
    }
    
    st.header(f"{group_names[st.session_state.current_group]} - Work Area")
    st.write(group_instructions[st.session_state.current_group])
    
    if st.session_state.task_input:
        st.info(f"**Your Task:** {st.session_state.task_input}")
    
    response = st.text_area(
        "Enter your solution here:",
        value=st.session_state.responses[st.session_state.current_group],
        height=300,
        key=f"response_{st.session_state.current_group}"
    )
    
    if st.button("Save Solution"):
        st.session_state.responses[st.session_state.current_group] = response
        st.success("Solution saved! Move to the next group or compare results.")

st.divider()

# Results Comparison
if all(st.session_state.responses.values()):
    st.header("Compare Results")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Group 1: No AI")
        st.text_area("", value=st.session_state.responses['noAI'], height=200, disabled=True, key="compare_noAI")
    
    with col2:
        st.subheader("Group 2: With AI")
        st.text_area("", value=st.session_state.responses['withAI'], height=200, disabled=True, key="compare_withAI")
    
    with col3:
        st.subheader("Group 3: AI + Framework")
        st.text_area("", value=st.session_state.responses['withFramework'], height=200, disabled=True, key="compare_withFramework")
    
    st.warning("**Discussion Points:** Which approach was fastest? Which produced the best quality? How did the framework help Group 3?")
    
    if st.button("Reset All Responses"):
        st.session_state.responses = {'noAI': '', 'withAI': '', 'withFramework': ''}
        st.rerun()