function deleteNote(noteId) {
  fetch("/delete-note", {     //POST request from the delete-node endpoint
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => { window.location.href = "/";   //reload
  });
}
