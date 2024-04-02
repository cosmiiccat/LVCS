import React from "react";
import "./Repositories.css";
import { useNavigate } from "react-router-dom";

function Repositories({ repository }) {
  const navigate = useNavigate();
  const handleRepositoryClick = () => {
    navigate("/repositories");
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
