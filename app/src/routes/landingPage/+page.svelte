<script>
  // Get habits from database and store in array
  import { onMount } from "svelte";

  onMount(async () => {
    // Get username from localstorage
    let username = localStorage.getItem("username");
    let password = localStorage.getItem("password");
    let habit = document.querySelector("#habit-list-update").value;
    localStorage.setItem("habit", habit);
    // Get habits from database http://localhost:5000/api/get_habits/username/password
    habits = await getHabits(username, password);
  });

  let habits = [""];
  // On mount, get habits from database

  async function updateHabit(event) {
    event.preventDefault();
    let habit = document.querySelector("#habit-list-update").value;
    localStorage.setItem("habit", habit);

    //open page updateHabit
    window.location.href = "/updateHabit";

    // Check if habits array is empty
    if (habits.length === 0) {
      alert("You have no habits to update");
      return;
    }
  }

  async function deleteHabit(event) {
    event.preventDefault();
    let username = localStorage.getItem("username");
    let password = localStorage.getItem("password");
    let habit_name = document.querySelector("#habit-list").value;

    // Check if habits array is empty
    if (habits.length === 0) {
      alert("You have no habits to delete");
      return;
    }

    const response = await fetch(
      `http://localhost:5000/api/delete_habit/${username}/${password}/${habit_name}`,
      {
        method: "DELETE",
      }
    );
    if (response.ok) {
      alert("Habit Deleted Successfully");
      habits = await getHabits(username, password);
    }
  }

  async function logout(){
    localStorage.clear();
    window.location.href = "/login";
  }

  async function getHabits(username, password) {
    const response = await fetch(
      "http://localhost:5000/api/get_user_habits/" + username + "/" + password,
      {
        method: "GET",
      }
    );
    const data = await response.json();
    const habits = [];
    for (let i = 0; i < data.length; i++) {
      const habit = data[i];
      habits.push([habit[2], habit[3], habit[4], habit[5]]);
    }
    return habits;
  }
</script>

<head>
  <title>My Landing Page</title>
</head>
<body>
  <div class="tiles">
    <div class="tile">
      <h2>Graph Placeholder</h2>
      <div class="graph-placeholder" />
    </div>
    <div class="tile">
      <h2>Create Habits</h2>
      <a href="/createHabit"><button>Create</button></a>
    </div>
    <div class="tile">
      <h2>Delete Habits</h2>
      <button id="delete-btn" on:click={deleteHabit}>Delete</button>
      <h3>List of Habits</h3>
      <select id="habit-list">
        {#each habits as habit}
          <option value={habit[0]}>{habit[0]}</option>
        {/each}
      </select>
    </div>
    <div class="tile">
      <h2>Update Current Habits</h2>
      <button on:click={updateHabit}>Update</button>
      <h3>List of Habits</h3>
      <select id="habit-list-update">
        {#each habits as habit}
          <option value={habit[0]}>{habit[0]}</option>
        {/each}
      </select>
    </div>
    <table>
      <thead>
        <tr>
          <th>Habit Name</th>
          <th>Metric Name</th>
          <th>Metric Value</th>
          <th>Goal Value</th>
        </tr>
      </thead>
      <tbody>
        {#each habits as habit}
        <tr>
          {#each habit as value}
          <td>{value}</td>
          {/each}
        </tr>
        {/each}
      </tbody>
    </table>
    <button class= "logout-button"on:click={logout}>Logout</button>
  </div>
</body>

<style>
  body {
    background-color: #f2f2f2;
    font-family: Arial, sans-serif;
  }
  .tiles {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    margin-top: 50px;
  }

  .tile {
    width: 300px;
    height: 200px;
    margin: 20px;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    text-align: center;
  }

  .graph-placeholder {
    width: 100%;
    height: 150px;
    border: 1px dashed #ccc;
    margin-top: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  button {
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
  }

  button:hover {
    background-color: #0069d9;
  }

  .logout-button {
  background-color: #f44336;
  border: none;
  color: #fff;
  margin-top: 20px;
  padding: 12px 24px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 4px;
  cursor: pointer;
}

.logout-button:hover {
  background-color: #d32f2f;
}

</style>
