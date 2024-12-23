export default function getListStudents() {
  const listStudents = [
    { id: 1, firstName: "Guillaume", location: "San Francisco" },
    { id: 2, firstName: "James", location: "Columbia" },
    { id: 5, firstName: "Serena", location: "San Francisco" },
  ];

  return listStudents.map((student) => ({
    id: student.id,
    firstName: student.firstName,
    location: student.location,
  }));
}
