// import { useEffect, useState } from "react";
// import { Link } from "react-router-dom";

function Home() {

  // function fetchResearch(){
  //   fetch("http://localhost:5555/research")
  //   .then(res => res.json())
  //   .then(res => console.log(res))
  //   .catch(err => console.log(err))
  // }

  // function fetchResearchById(){
  //   fetch("http://localhost:5555/research/1")
  //   .then(res => res.json())
  //   .then(res => console.log(res))
  //   .catch(err => console.log(err))
  // }

  // function deleteResearchById(){
  //   fetch("http://localhost:5555/research/1", {
  //     method: "DELETE"
  //   })
  //   .then(res => res.json())
  //   .then(res => console.log(res))
  //   .catch(err => console.log(err))
  // }


  // function fetchAuthors(){
  //   fetch("http://localhost:5555/authors")
  //   .then(res => res.json())
  //   .then(res => console.log(res))
  //   .catch(err => console.log(err))
  // }
  

  return (
    <section className="container">
      <div>Test</div>
      <div>
        {/* <p>Test get /research, click on <a onClick={()=> fetchResearch()}>this</a> and view the json or error in the console!</p>
        <p>Test get /research/id, click on <a onClick={()=> fetchResearchById()}>this</a> and view the json or error in the console!</p>
        <p>Test delete /research/id, click on <a onClick={()=> deleteResearchById()}>this</a> and view the json or error in the console!</p>
        <p>Test get /authors, click on <a onClick={()=> fetchAuthors()}>this</a> and view the json or error in the console!</p> */}
      </div>
    </section>
  );
}

export default Home;
