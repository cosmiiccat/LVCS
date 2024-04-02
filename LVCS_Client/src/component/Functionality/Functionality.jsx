import React from "react";
import { useNavigate } from "react-router-dom";
import { useRef, useState } from "react";

import logo from "../../assets/github-mark.svg";

import "./Functionality.css";
function Functionality() {
  const navigate = useNavigate();
  const [additionalComponent, setAdditionalComponent] = useState(false);
  const [additionalComponentforInit, setAdditionalComponentforInit] = useState(false);
  const [pathUrl, setPathUrl] = useState("");
  const [pathUrlforInit, setPathUrlforInit] = useState("");
  const [pathExist, setPathExist] = useState(false);


  const pathRef = useRef(null);
  const parthRefforInit = useRef(null);

  const handleINITbutton = () => {
    setAdditionalComponentforInit(!additionalComponentforInit);
    parthRefforInit.current.style.position = "absolute";
  };

  const handleADDbutton = () => {};

  const handleCOMMITbutton = () => {};

  const handlePULLbutton = () => {};

  const handlePUSHbutton = () => {};

  const handleCLONEbutton = () => {};

  return (
    <div className="FunctionalityParentContainer">
      <div className="MainPageMainContainer">
        <div className="LVCS-Logo">
          <img src={logo} alt="LVCS Logo" />
        </div>

        {additionalComponentforInit && (
          <div className="Take-Input" ref={parthRefforInit}>
            {pathExist ? (
            <div>
                <div className="Path-Url">{pathUrlforInit}</div>
                <button className="Submit-Button">Submit</button>
            </div>
            ) : (
            <div>
                <input
                type="text"
                className="Path"
                placeholder="Enter the path"
                value={pathUrlforInit}
                onChange={(e) => setPathUrlforInit(e.target.value)}
                
                />
                <button className="Submit-Button" onClick={setPathExist(true)}>Submit</button>
            </div>
            )}
            
          </div>
        )}

        <div className="ButtonAndInput">
          <div class="ButtonContainer">
            <div class="row">
              <button class="function-button" onClick={handleINITbutton}>
                init
              </button>
              <button class="function-button" onClick={handleADDbutton}>
                add
              </button>
              <button class="function-button" onClick={handleCOMMITbutton}>
                commit
              </button>
            </div>
            <div class="row">
              <button class="function-button" onClick={handlePULLbutton}>
                pull
              </button>
              <button class="function-button" onClick={handlePUSHbutton}>
                push
              </button>
              <button class="function-button" onClick={handleCLONEbutton}>
                clone
              </button>
            </div>
          </div>

          {additionalComponent && (
            <div className="Take-Input" ref={pathRef}>
              <input
                type="text"
                className="Path"
                placeholder="Enter the path"
                value={pathUrl}
                onChange={(e) => setPathUrl(e.target.value)}
              />
              <button className="Submit-Button">Submit</button>
            </div>
          )}
        </div>
      </div>
      <div className="ExtraThing">
        <p>hello</p>
      </div>
    </div>
  );
}

export default Functionality;
