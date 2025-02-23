document.addEventListener("DOMContentLoaded", function () {
  fetchTasks(); // Load tasks when the page loads
});

// Fetch all tasks from Django API
async function fetchTasks() {
  try {
    let response = await fetch("/api/tasks/");
    let tasks = await response.json();
    let taskList = document.getElementById("taskList");
    taskList.innerHTML = "";

    tasks.forEach((task) => {
      let li = document.createElement("li");
      li.innerHTML = `
                ${task.title} 
                <button onclick="deleteTask(${task.id})">Delete</button>
                <input type="checkbox" ${
                  task.completed ? "checked" : ""
                } onchange="updateTask(${task.id}, this.checked)">
            `;
      taskList.appendChild(li);
    });
  } catch (error) {
    console.error("Error fetching tasks:", error);
  }
}

// Add a new task
async function addTask() {
  let taskInput = document.getElementById("taskInput");
  let title = taskInput.value.trim();
  if (!title) return alert("Task cannot be empty!");

  try {
    let response = await fetch("/api/tasks/add/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title }),
    });
    if (response.ok) {
      taskInput.value = ""; // Clear input box
      fetchTasks(); // Refresh task list
    }
  } catch (error) {
    console.error("Error adding task:", error);
  }
}

// Delete a task
async function deleteTask(id) {
  try {
    let response = await fetch(`/api/tasks/delete/${id}/`, {
      method: "DELETE",
    });
    if (response.ok) fetchTasks(); // Refresh task list
  } catch (error) {
    console.error("Error deleting task:", error);
  }
}

// Update task completion status
async function updateTask(id, completed) {
  try {
    let response = await fetch(`/api/tasks/update/${id}/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ completed }),
    });
    if (response.ok) fetchTasks(); // Refresh task list
  } catch (error) {
    console.error("Error updating task:", error);
  }
}
