import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useRef, useState } from "react";
import { useContext } from "react";
import axios from "axios";

import AllContext from "../../context/AllContext";

import logo from "../../assets/github-mark.svg";

import "./Functionality.css";
import ContentPage from "../ContentPage/ContentPage";
import RepositoryPage from "../RepositoryPage/RepositoryPage";
function Functionality() {
  const { INITpath, setINITpath } = useContext(AllContext);
  const navigate = useNavigate();
  const [additionalComponent, setAdditionalComponent] = useState(false);
  const [additionalComponentforInit, setAdditionalComponentforInit] =
    useState(false);
  const [additionalComponentforCommit, setAdditionalComponentforCommit] =
    useState(false);
  const [pathUrl, setPathUrl] = useState("");
  const [pathUrlforInit, setPathUrlforInit] = useState("");
  const [pathExist, setPathExist] = useState(false);
  const [payload, setPayload] = useState({});
  const [commitPayload, setCommitPayload] = useState({});
  const [commitMessage, setCommitMessage] = useState("");
  const [commitStatus, setCommitStatus] = useState(false);
  const [currentStatus, setCurrentStatus] = useState("local");

  const pathRef = useRef(null);
  const parthRefforInit = useRef(null);
  const commitRef = useRef(null);

  const handleINITbutton = () => {
    setAdditionalComponentforInit(true);
  };

  useEffect(() => {
    const localButton = document.querySelector(".local-button");
    const remoteButton = document.querySelector(".remote-button");

    if(currentStatus === "local"){
      localButton.classList.add("active");
      remoteButton.classList.remove("active");
    }
    if(currentStatus === "remote"){
      remoteButton.classList.add("active");
      localButton.classList.remove("active");
    }
  }, [currentStatus]);

  const handleLocal = () => {
    setCurrentStatus("local");
  };

  const handleRemote = () => {
    setCurrentStatus("remote");
  };


  const handleADDbutton = () => {
    axios
      .post("http://127.0.0.1:8000/lvcs/add", payload)
      .then((res) => {
        console.log(res);
        consoleLog(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const handleCOMMITbutton = () => {
    setAdditionalComponentforCommit(!additionalComponentforCommit);
  };

  const handleCommitMessage = () => {
    if (!commitMessage) return;
    setCommitStatus(true);
    console.log("This is the commit message: ", commitMessage);
    const COMMITpayload = {
      path: pathUrl,
      commit: true,
      commit_message: commitMessage,
    };
    setCommitPayload(COMMITpayload);
    axios
      .post("http://127.0.0.1:8000/lvcs/commit", COMMITpayload)
      .then((res) => {
        console.log(res);
        consoleLog(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
    setAdditionalComponentforCommit(!additionalComponentforCommit);
  };

  const handlePULLbutton = () => {
    axios
    .post("http://127.0.0.1:8000/lvcs/pull", payload)
      .then((res) => {
        console.log(res);
        consoleLog(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const handlePUSHbutton = () => {
    console.log("This is the payload: ", payload);
    axios
    .post("http://127.0.0.1:8000/lvcs/push", payload)
      .then((res) => {
        console.log(res);
        consoleLog(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const handleCLONEbutton = () => {
    console.log("This is the payload: ", payload);
    axios
    .post("http://127.0.0.1:8000/lvcs/clone", payload)
      .then((res) => {
        console.log(res);
        consoleLog(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const consoleLog = (data) => {
    const ul = document.querySelector(".lines");
    const div = document.createElement("div");
    const span = document.createElement("span");
    const p = document.createElement("p");

    if(data.success === "false"){
      p.className = "error";
      p.textContent = data.error;
    }else{
      p.className = "success";
      p.textContent = data.data;
    }

    div.className = "console-log-message";
    span.className = "console-log";
    span.textContent = pathUrl;
    // p.textContent = data.message;
    div.append(span, p);
    ul.appendChild(div);
  };

  const handlePathExist = () => {
    if (!pathExist) setPathUrl(pathUrl);
    if (!pathUrl) return;
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
        consoleLog(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  useEffect(() => {
    console.log("This is the path: ", pathUrl);
  }, [pathUrl]);

  return (
    <div className="Parent">

      <div className="nav-bar">
        <button className="local-button" onClick={handleLocal}>local</button>
        <button className="remote-button" onClick={handleRemote}>remote</button>
      </div>

    {currentStatus === "local" ? (
    <div className="FunctionalityParentContainer">
      <div className="MainPageMainContainer">
        <div className="LVCS-Logo">
          <img src={logo} alt="LVCS Logo" />
        </div>

        {additionalComponentforInit && (
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

        )}

        {additionalComponentforCommit &&
          (commitStatus ? (
            <div className="CommitContainer PathContainer"> Last Commit: <span className="Last-Commit">{commitMessage}</span> </div>
          ) : (
            <div className="CommitContainer PathContainer">
              <input
                type="text"
                className="commit-message Path"
                placeholder="Enter commit message"
                value={commitMessage}
                onChange={(e) => setCommitMessage(e.target.value)}
              />
              <div className="set-commit-message-button">
                <button
                  className="Submit-Button Set-Button commit-button"
                  onClick={handleCommitMessage}
                >
                  Commit Changes
                </button>
              </div>
            </div>
          ))}

        

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
        <ul className="lines"></ul>
      </div>
    </div>
    ) :(
      <div className="RepositoryPage-Component">
        <RepositoryPage/>
      </div>
    )}
    </div>
  );
}

export default Functionality;
