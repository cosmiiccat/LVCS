import React from "react";
import "./Content.css";
import { useState } from "react";
import {useContext} from "react";
import AllContext from "../../context/AllContext";
import { Navigate } from "react-router-dom";

import FileIcon from "../../assets/file.svg";
import FolderIcon from "../../assets/folder.svg";

function Content({ name, icon, message, date,data }) {

  
  const {currentData,setCurrentData,setCurrentDirectory,currentDirectory} = useContext(AllContext);
	const handleOpenContent = () => {
		setCurrentData(data);
    setCurrentDirectory(currentDirectory + "/" + name);
    let dir = currentDirectory + "/" + name
    dir = dir.split("/");
    dir = dir.join(".");
    console.log("This is dir from open: ",String(dir));
	}

  return (
    <div className="ContentMainContainer">

      <div className="NameAndIcon">
        <div className="ContentIcon">
          {icon === "folder" ? (
            <img src={FolderIcon} className="FolderIcon" alt="FolderIcon" />
          ) : (
            <img src={FileIcon} className="FileIcon" alt="FileIcon" />
          )}
        </div>
        <div className="ContentName" onClick={handleOpenContent}>{name} </div>
      </div>

      <div className="CommitMessage">
        <div className="CommitMessageText">{message}</div>
      </div>

      <div className="CommitDate">
        <div className="CommitDateText">{date}</div>
      </div>
    </div>
  );
}

export default Content;
