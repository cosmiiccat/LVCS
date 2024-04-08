import React from "react";
import { useState } from "react";
import "./RepositoryPage.css";

import Repositories from "../Repositories/Repositories";

function RepositoryPage() {
  const [repositories, setRepositories] = useState([
    {
      id: 1,
      name: "Repository 1",
      sector: "Private",
      description: "Description 1",
      technology: "Html",
    },
    {
      id: 2,
      name: "Repository 2",
      sector: "Public",
      description: "Description 2",
      technology: "JavaScript",
    },
    {
      id: 3,
      name: "Repository 3",
      sector: "Public",
      description: "Description 3",
      technology: "JavaScript",
    },
    {
      id: 4,
      name: "Repository 4",
      sector: "Public",
      description: "Description 4",
      technology: "JavaScript",
    },
    
    
  ]);
  console.log(repositories);
  return (
    <div className="Repository">
      <div className="Heading"><h1>Available Repositories</h1></div>
      
      {/* <div className="checking"> */}
      <div className="RepositoryContainer">
        
        {repositories.map((repository) => {
          return  <Repositories key={repository.id} repository={repository} />;
        })}
      </div>
      {/* </div> */}
    </div>
  );
}

export default RepositoryPage;
