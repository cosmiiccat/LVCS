import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useRef, useState } from "react";
import { useContext } from "react";
import axios from "axios";

import AllContext from "../../context/AllContext";

import logo from "../../assets/github-mark.svg";

import "./Functionality.css";
function Functionality() {
  const { INITpath, setINITpath } = useContext(AllContext);
  const navigate = useNavigate();
  const [additionalComponent, setAdditionalComponent] = useState(false);
  const [additionalComponentforInit, setAdditionalComponentforInit] =
    useState(false);
  const [pathUrl, setPathUrl] = useState("");
  const [pathUrlforInit, setPathUrlforInit] = useState("");
  const [pathExist, setPathExist] = useState(false);
  const [payload, setPayload] = useState({});

  const pathRef = useRef(null);
  const parthRefforInit = useRef(null);

  const handleINITbutton = () => {
    setAdditionalComponentforInit(!additionalComponentforInit);
  };

  const handleADDbutton = () => {};

  const handleCOMMITbutton = () => {};

  const handlePULLbutton = () => {};

  const handlePUSHbutton = () => {};

  const handleCLONEbutton = () => {};

  const handlePathExist = () => {
    if (!pathExist) setPathUrl(pathUrl);
    setPathExist(true);
    setINITpath(pathUrl);
    const payload = {
      path: pathUrl,
    };
    setPayload(payload);
    console.log("This is path", pathUrl);
    console.log(payload);

    axios
      .post("http://127.0.0.1:8000/lvcs/init", payload)
      .then((res) => {
        console.log(res);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  useEffect(() => {
    console.log("This is the path: ", pathUrlforInit);
  }, [pathUrlforInit]);

  return (
    <div className="FunctionalityParentContainer">
      <div className="MainPageMainContainer">
        <div className="LVCS-Logo">
          <img src={logo} alt="LVCS Logo" />
        </div>

        <div className="PathContainer">
          
          <input
            type="text"
            className="Path"
            placeholder="Enter the path"
            value={pathUrl}
            onChange={(e) => setPathUrl(e.target.value)}
          />
          <div className="set-reset-buttons">
            <button
              className="Submit-Button Set-Button"
              onClick={handlePathExist}
            >
              Set
            </button>
            <button
              className="Submit-Button Reset-Button"
              onClick={handlePathExist}
            >
              Reset
            </button>
          </div>
        </div>

        {additionalComponentforInit && (
          <div className="Take-Input" ref={parthRefforInit}>
            {pathExist && (
              <div>
                <div className="Message">Initialization done</div>
                <div className="Path-Url">
                  Path initialized for:{" "}
                  <span className="Message2">/home/iayushch/Desktop/temp</span>
                </div>
                {/* <button className="Submit-Button">Submit</button> */}
              </div>
            )}
          </div>
        )}

        <div className="ButtonAndInput">
          <div className="ButtonContainer">
            <div className="row">
              <button className="function-button" onClick={handleINITbutton}>
                init
              </button>
              <button className="function-button" onClick={handleADDbutton}>
                add
              </button>
              <button className="function-button" onClick={handleCOMMITbutton}>
                commit
              </button>
            </div>
            <div className="row">
              <button className="function-button" onClick={handlePULLbutton}>
                pull
              </button>
              <button className="function-button" onClick={handlePUSHbutton}>
                push
              </button>
              <button className="function-button" onClick={handleCLONEbutton}>
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
      <div className="ExtraThing console">
        <div className="console-heading">
          <h1>Console</h1>
        </div>
        <ul className="lines">
          <p>asdfsadfsdf</p>
        </ul>
      </div>
    </div>
  );
}

export default Functionality;
