function showSection(sectionId) {
  const sections = document.querySelectorAll(".content-section");
  const buttons = document.querySelectorAll(".menu-item");

  sections.forEach(section => {
    section.classList.remove("active-section");
  });

  buttons.forEach(button => {
    button.classList.remove("active");
  });

  document.getElementById(sectionId).classList.add("active-section");

  event.target.classList.add("active");
}