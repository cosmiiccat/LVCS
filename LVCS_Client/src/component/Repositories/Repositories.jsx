import React from "react";
import "./Repositories.css";
import axios from "axios";


import { useNavigate } from "react-router-dom";
import { useContext } from "react";

import AllContext from "../../context/AllContext";

function Repositories({ repository }) {
  const { currentDirectory, setCurrentDirectory } = useContext(AllContext);
  const navigate = useNavigate();
  const handleRepositoryClick = () => {
    axios
      .get("http://127.0.0.1:8000/lvcs/repository")
      .then((response) => {
        console.log(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
    navigate("/contentpage");
  };
  return (
    <div className="RepositoriesMainContainer">
      <div className="NameAndSector">
        <div className="RepositoryName" onClick={handleRepositoryClick}>
          {repository.name}
        </div>
        <div className="RepositorySector">{repository.sector}</div>
      </div>
      <div className="RepositoryDescription">
        <div className="Description">{repository.description}</div>
      </div>
      <div className="Technology">{repository.technology}</div>
    </div>
  );
}

export default Repositories;
