import React from "react";
import "./ContentPage.css";
import { useState } from "react";
import { useContext } from "react";
import AllContext from "../../context/AllContext";

import arrow from "../../assets/arrow.svg";

import Content from "../Content/Content";

function ContentPage() {
  const { currentData,currentDirectory,setCurrentDirectory,setCurrentData,data } = useContext(AllContext);

  const handleGoBack = () => {
    let temp = currentDirectory.split("/");
    temp.pop();
    temp = temp.join("/");
    console.log(temp);
    setCurrentDirectory(temp);
    
    let keys  = temp.split("/");
    console.log(keys);
    let tempData = data;

    keys.shift();

    if(keys.length === 0){
      setCurrentData(data);
      return;
    }

    keys.forEach((key) => {
      tempData = tempData[key];
    });

    setCurrentData(tempData);
  }

  return (
    <div className="ContentPageMainContainer">
      <div className="CurrentDirectory">
        
        <img src={arrow} className="back-arrow" alt="Go Back" onClick={handleGoBack} />
        <span><b>Directory: </b>  {currentDirectory}</span>

      </div>
      <div className="ContentContainer">
		
        {Object.keys(currentData).map((key) => {
			if(key !== "CommitMessage" && key !== "CommitDate"){

		  return (
			<div key={key} className="EachContent">
			<Content
			  key={key}
        data={currentData[key]}
			  name={key}
			  icon={typeof currentData[key] === "object" ? "folder" : "file"}
			  message={currentData.CommitMessage}
			  date={currentData.CommitDate}
			/>
			</div>
		  );}
		})}
		
      </div>
    </div>
  );
}

export default ContentPage;
