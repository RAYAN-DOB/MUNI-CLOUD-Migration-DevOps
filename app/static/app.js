async function init() {
  const health = document.getElementById("health");
  const list = document.getElementById("services");
  try {
    const response = await fetch("/api/info", {cache: "no-store"});
    if (!response.ok) throw new Error("HTTP " + response.status);
    const data = await response.json();
    health.textContent = "API du labo accessible";
    document.getElementById("version").textContent = "VERSION : " + data.version;
    for (const item of data.services) {
      const row = document.createElement("div");
      row.className = "service";
      const icon = document.createElement("span");
      icon.className = "service-icon";
      icon.textContent = "▤";
      const info = document.createElement("div");
      const title = document.createElement("b");
      title.textContent = item.name;
      const hint = document.createElement("small");
      hint.textContent = item.category + " • Données fictives";
      info.append(title, hint);
      const state = document.createElement("span");
      state.className = "service-state";
      state.textContent = item.phase;
      row.append(icon, info, state);
      list.appendChild(row);
    }
  } catch {
    health.textContent = "API indisponible";
    list.textContent = "Le portail ne peut pas récupérer les services.";
  }
}
init();
