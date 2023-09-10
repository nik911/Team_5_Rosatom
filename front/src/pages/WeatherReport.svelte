<script>
  let info = {
    points: ["Саббета 1", "Саббета 2", "Саббета 3", "Точка в Баренцевом море"],
  };

  let data = { points: Array(info.points.length - 1) };

  const numbersOnly = (event) => {
    if (event.which < 48 || event.which > 57) event.preventDefault();
  };

  $: console.log(data);
</script>

<main>
  <div class="container">
    <header>
      <h1>Отчет погодных условий на месяц</h1>
    </header>
    <h5>Сплоченность льда на маршрутах (в баллах):</h5>
    {#each { length: info.points.length - 1 } as _, i}
      <label>{`${info.points[i]} → ${info.points[i + 1]}`}</label>
      <input
        type="number"
        placeholder="5"
        on:keypress={numbersOnly}
        bind:value={data.points[i]}
      />
    {/each}

    <button>Отправить отчет</button>
  </div>
</main>
