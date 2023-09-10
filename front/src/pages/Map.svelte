<script>
  // @ts-nocheck

  import { LeafletMap, TileLayer, GeoJSON } from "svelte-leafletjs";

  import geo from "../example.geo.json";

  const mapOptions = {
    center: [40, 90],
    zoom: 3,
    attributionControl: false,
    zoomControl: false,
  };
  const tileUrl = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
  const tileLayerOptions = {
    minZoom: 0,
    maxZoom: 20,
    maxNativeZoom: 19,
  };

  let leafletMap;

  console.log(geo);
</script>

<div class="board">
  <div class="sidebar">
    <h3>Мои суда</h3>
    <div class="list">
      <button class="outline contrast">Штурман Альбанов</button>
      <button class="outline contrast">Штурман Кошелев</button>
      <button class="outline contrast">Лагорта</button>
      <button class="outline contrast">Михаил Лазарев</button>
    </div>
    <div class="actions" role="group">
      <a role="button" class="primary" href="/#/application">Новая заявка</a>
      <a role="button" class="secondary" href="/#/chart">Расписание</a>
      <a role="button" class="secondary" href="/#/vessel">Добавить судно</a>
    </div>
  </div>
  <div class="map">
    <LeafletMap bind:this={leafletMap} options={mapOptions}>
      <TileLayer url={tileUrl} options={tileLayerOptions} />
      <GeoJSON data={geo} />
    </LeafletMap>
  </div>
</div>

<style>
  .board {
    height: 100vh;
    display: flex;
  }

  .map {
    width: 100%;
  }

  .sidebar {
    width: 800px;
    padding: 1rem;
    border-right: 1px solid black;
  }

  .list > button {
    width: 100%;
    text-align: start;
    margin-bottom: -1px;
    border-radius: 0;
  }

  .actions {
    margin-top: 1rem;
    margin-right: 4px;
  }
</style>
