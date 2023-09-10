<script>
  import Gantt from "frappe-gantt";
  import { onMount } from "svelte";

  Gantt.prototype.bind_events = () => {};

  let tasks = [
    {
      name: "Караван 1",
      start: new Date("2022-01-01 03:32"),
      end: new Date("2022-01-10 03:32"),
    },
    {
      name: "Караван 2",
      start: new Date("2022-01-03 03:32"),
      end: new Date("2022-01-15 03:32"),
    },
    {
      name: "Караван 3",
      start: new Date("2021-12-29 03:32"),
      end: new Date("2022-01-06 03:32"),
    },
  ];

  let gantt;

  onMount(() => {
    gantt = new Gantt("#gantt-wrapper", tasks, {
      view_mode: "Half Day",
      header_height: 50,
      bar_height: 75,
      padding: 50,
      language: "ru",
    });
  });
</script>

<div class="main">
  <h1>График отправления судов</h1>
  <div id="gantt-wrapper" />
  <div class="actions">
    <a href="/#/" role="button" class="secondary">Перейти на карту</a>
  </div>
</div>

<style>
  h1 {
    margin-top: 2rem;
    margin-bottom: 2rem;
  }

  #gantt-wrapper {
    width: calc(100vw - 64px);
    overflow: auto !important;
    box-shadow: 0 0 16px #00000020;
  }

  .main {
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .actions {
    margin-top: 2rem;
  }

  :global(text.bar-label) {
    fill: black !important;
    font-size: 20px !important;
  }
</style>
