<script>
  let data = {};

  $: console.log(data);

  const numbersOnly = (event) => {
    if (event.which < 48 || event.which > 57) event.preventDefault();
  };
</script>

<main>
  <div class="container">
    <header>
      <h1>Новое судно</h1>
    </header>
    <label>Наименование</label>
    <input placeholder="Михаил Лазарев" bind:value={data.name} />
    <label>IMO</label>
    <input
      type="number"
      placeholder="9837547"
      on:keypress={numbersOnly}
      bind:value={data.imo}
    />
    <label>Ледовый класс</label>
    <select required bind:value={data.iceClass}>
      <option>No ice class</option>
      <option>Ice1</option>
      <option>Ice2</option>
      <option>Ice3</option>
      <option>Arc4</option>
      <option>Arc5</option>
      <option>Arc6</option>
      <option>Arc7</option>
      <option>Arc8</option>
      <option>Arc9</option>
    </select>
    <label>Скорость (в узлах)</label>
    <input
      type="number"
      placeholder="15"
      on:keypress={numbersOnly}
      bind:value={data.speed}
    />
    <button>Добавить судно</button>
  </div>
</main>
