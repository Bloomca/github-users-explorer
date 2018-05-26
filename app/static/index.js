const input = document.getElementById("search");
const link = document.getElementById("search-link");

input.addEventListener("input", e => {
  const value = e.target.value;

  link.setAttribute("formaction", makeLink(value));
});

function makeLink(username) {
  return `/users/${username}`;
}
