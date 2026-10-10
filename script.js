const projects = [
  { week: 1, title: "My interactive CV" },
  { week: 2, title: "Basic Algorithms" },
  { week: 3, title: "Sorting Visualiser" },
  { week: 4, title: "Binary Search Visualisation" },
  { week: 5, title: "Sorting Race" },
  { week: 6, title: "Genetic algorithms"}
];

const container = document.getElementById('projects-container');

projects.forEach(proj => {
  const card = document.createElement('div');
  card.className = 'card';
  card.innerHTML = `<h2>Week ${proj.week}</h2><p>${proj.title}</p>`;
  card.onclick = () => {
    window.location.href = `week${proj.week}/docs/index.html?mode=app`;
  };
  container.appendChild(card);
});

// Fade-in animation on load
window.addEventListener('DOMContentLoaded', () => {
  const cards = document.querySelectorAll('.card');
  cards.forEach((card, index) => {
    card.style.opacity = 0;
    card.style.transform = "translateY(20px)";
    setTimeout(() => {
      card.style.transition = "all 0.6s ease";
      card.style.opacity = 1;
      card.style.transform = "translateY(0)";
    }, index * 100);
  });
});