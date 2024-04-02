import React from "react";
import { useNavigate } from "react-router-dom";

import logo from "../../assets/github-mark.svg";

import "./MainPage.css";
function MainPage() {
  const navigate = useNavigate();

  const handleConnectButtonClick = () => {
    navigate("/repositories");
  };

  return (
    <div className="MainPageMainContainer">
      <div className="LVCS-Logo">
        <img src={logo} alt="LVCS Logo" />
      </div>
      <div className="FeatureAndConnectContainer">
        <div className="Features">
          <div className="FeatureContainer">
            <div className="Feature1 Feature-Card">
              <h1>Feature 1</h1>
              <ul>
                <li>View all repositories</li>
                <li>View all commits</li>
                <li>View all pull requests</li>
              </ul>
            </div>

            <div className="Feature1 Feature-Card">
              <h1>Feature 1</h1>
              <ul>
                <li>View all repositories</li>
                <li>View all commits</li>
                <li>View all pull requests</li>
              </ul>
            </div>

            <div className="Feature2 Feature-Card">
              <h1>Feature 2</h1>
              <ul>
                <li>View all issues</li>
                <li>View all branches</li>
                <li>View all tags</li>
              </ul>
            </div>
            <div className="Feature3 Feature-Card">
              <h1>Feature 3</h1>
              <ul>
                <li>View all issues</li>
                <li>View all branches</li>
                <li>View all tags</li>
              </ul>
            </div>
          </div>
        </div>
        <div className="ConnectButton">
          <button className="button" onClick={handleConnectButtonClick}>
            Connect
          </button>
        </div>
      </div>
    </div>
  );
}

export default MainPage;
