<head>
  <title>Create Habit</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link rel="stylesheet" type="text/css" href="styles.css" />
</head>
<body>
  <div class="form-wrapper">
    <h1>Create Habit</h1>
    <form method="POST" action="submit_habit.php">
      <label for="habit-name">Habit Name:</label>
      <input type="text" id="habit-name" name="habit_name" required />
      <label for="metric-name">Metric Name:</label>
      <input type="text" id="metric-name" name="metric_name" required />
      <label for="metric-value">Metric Value:</label>
      <input
        type="number"
        id="metric-value"
        name="metric_value"
        step="0.01"
        required
      />
      <label for="goal-value">Goal Value:</label>
      <input
        type="number"
        id="goal-value"
        name="goal_value"
        step="0.01"
        required
      />
      <button type="submit">Create</button>
    </form>
  </div>
</body>

<style>
  body {
    background-color: #f2f2f2;
    font-family: Arial, sans-serif;
  }
  .form-wrapper {
    width: 90%;
    margin: 0 auto;
    margin-top: 50px;
    text-align: center;
  }

  h1 {
    margin-bottom: 30px;
  }

  form {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  label {
    margin-top: 20px;
    text-align: left;
  }

  input {
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ccc;
    margin-top: 5px;
    width: 100%;
    max-width: 300px;
  }

  button[type="submit"] {
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    margin-top: 20px;
    width: 100%;
    max-width: 300px;
  }

  button[type="submit"]:hover {
    background-color: #0069d9;
  }
</style>
