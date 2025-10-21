import React, { useState } from 'react';
import { Clock, Users, Lightbulb, Zap, CheckCircle } from 'lucide-react';

export default function AIWorkshopSandbox() {
  const [currentGroup, setCurrentGroup] = useState(null);
  const [taskInput, setTaskInput] = useState('');
  const [responses, setResponses] = useState({
    noAI: '',
    withAI: '',
    withFramework: ''
  });

  const groups = [
    {
      id: 'noAI',
      name: 'Group 1: No AI',
      icon: Users,
      color: 'bg-gray-100 border-gray-300',
      description: 'Complete the task without any AI assistance',
      instructions: 'Work together as a team to solve the problem using traditional methods.'
    },
    {
      id: 'withAI',
      name: 'Group 2: With AI',
      icon: Lightbulb,
      color: 'bg-blue-100 border-blue-300',
      description: 'Use AI to help complete the task',
      instructions: 'Use an AI tool with your own prompts to solve the problem.'
    },
    {
      id: 'withFramework',
      name: 'Group 3: AI + Framework',
      icon: Zap,
      color: 'bg-purple-100 border-purple-300',
      description: 'Use AI with our prompting framework',
      instructions: 'Apply the framework below to structure your AI prompts.'
    }
  ];

  const framework = {
    title: 'Effective Prompting Framework',
    steps: [
      { label: 'Context', description: 'Provide background information and relevant details' },
      { label: 'Task', description: 'Clearly state what you want the AI to do' },
      { label: 'Format', description: 'Specify the desired output format' },
      { label: 'Constraints', description: 'Set any limitations or requirements' },
      { label: 'Examples', description: 'Include examples if helpful' }
    ]
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-50 to-purple-50 p-8">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="bg-white rounded-lg shadow-lg p-8 mb-8">
          <h1 className="text-4xl font-bold text-gray-800 mb-4">
            Phase 2: Interactive AI Sandbox
          </h1>
          <p className="text-lg text-gray-600 mb-4">
            Split into three groups and complete the same task using different approaches. 
            <strong className="text-indigo-600"> Each group should time themselves</strong> to compare efficiency.
          </p>
          <div className="flex items-center gap-2 bg-yellow-50 border border-yellow-200 rounded-lg p-4">
            <Clock className="text-yellow-600" size={24} />
            <span className="text-gray-700 font-medium">Facilitator: Start timing each group when they begin!</span>
          </div>
        </div>

        {/* Task Input Section */}
        <div className="bg-white rounded-lg shadow-lg p-8 mb-8">
          <h2 className="text-2xl font-bold text-gray-800 mb-4">Workshop Task</h2>
          <p className="text-gray-600 mb-4">Facilitator: Enter the task all groups will complete</p>
          <textarea
            value={taskInput}
            onChange={(e) => setTaskInput(e.target.value)}
            placeholder="Example: Write a professional email declining a meeting invitation while suggesting alternative times..."
            className="w-full h-32 p-4 border-2 border-gray-300 rounded-lg focus:outline-none focus:border-indigo-500"
          />
        </div>

        {/* Group Selection */}
        <div className="grid md:grid-cols-3 gap-6 mb-8">
          {groups.map((group) => {
            const Icon = group.icon;
            return (
              <button
                key={group.id}
                onClick={() => setCurrentGroup(group.id)}
                className={`${group.color} border-2 rounded-lg p-6 text-left transition-all hover:shadow-lg ${
                  currentGroup === group.id ? 'ring-4 ring-indigo-300' : ''
                }`}
              >
                <Icon size={32} className="mb-3 text-gray-700" />
                <h3 className="text-xl font-bold text-gray-800 mb-2">{group.name}</h3>
                <p className="text-gray-600 text-sm">{group.description}</p>
              </button>
            );
          })}
        </div>

        {/* Framework Display for Group 3 */}
        {currentGroup === 'withFramework' && (
          <div className="bg-gradient-to-r from-purple-50 to-indigo-50 border-2 border-purple-300 rounded-lg p-8 mb-8">
            <h2 className="text-2xl font-bold text-gray-800 mb-6 flex items-center gap-2">
              <Zap className="text-purple-600" size={28} />
              {framework.title}
            </h2>
            <div className="space-y-4">
              {framework.steps.map((step, index) => (
                <div key={index} className="bg-white rounded-lg p-4 shadow-sm">
                  <div className="flex items-start gap-3">
                    <div className="bg-purple-600 text-white rounded-full w-8 h-8 flex items-center justify-center font-bold flex-shrink-0">
                      {index + 1}
                    </div>
                    <div>
                      <h4 className="font-bold text-gray-800 mb-1">{step.label}</h4>
                      <p className="text-gray-600 text-sm">{step.description}</p>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Work Area */}
        {currentGroup && (
          <div className="bg-white rounded-lg shadow-lg p-8">
            <h2 className="text-2xl font-bold text-gray-800 mb-4">
              {groups.find(g => g.id === currentGroup)?.name} - Work Area
            </h2>
            <p className="text-gray-600 mb-6">
              {groups.find(g => g.id === currentGroup)?.instructions}
            </p>
            
            {taskInput && (
              <div className="bg-indigo-50 border border-indigo-200 rounded-lg p-4 mb-6">
                <h3 className="font-bold text-gray-800 mb-2">Your Task:</h3>
                <p className="text-gray-700">{taskInput}</p>
              </div>
            )}

            <textarea
              value={responses[currentGroup]}
              onChange={(e) => setResponses({...responses, [currentGroup]: e.target.value})}
              placeholder="Enter your solution here..."
              className="w-full h-64 p-4 border-2 border-gray-300 rounded-lg focus:outline-none focus:border-indigo-500 mb-4"
            />
            
            <button
              onClick={() => alert('Solution saved! Move to the next group or compare results.')}
              className="bg-indigo-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-indigo-700 transition-colors flex items-center gap-2"
            >
              <CheckCircle size={20} />
              Save Solution
            </button>
          </div>
        )}

        {/* Results Comparison (shows when all groups have input) */}
        {responses.noAI && responses.withAI && responses.withFramework && (
          <div className="mt-8 bg-white rounded-lg shadow-lg p-8">
            <h2 className="text-2xl font-bold text-gray-800 mb-6">Compare Results</h2>
            <div className="grid md:grid-cols-3 gap-6">
              {groups.map((group) => (
                <div key={group.id} className="border-2 border-gray-200 rounded-lg p-4">
                  <h3 className="font-bold text-gray-800 mb-3">{group.name}</h3>
                  <div className="bg-gray-50 rounded p-3 text-sm text-gray-700 max-h-48 overflow-y-auto">
                    {responses[group.id] || 'No response yet'}
                  </div>
                </div>
              ))}
            </div>
            <div className="mt-6 bg-yellow-50 border border-yellow-200 rounded-lg p-4">
              <p className="text-gray-700">
                <strong>Discussion Points:</strong> Which approach was fastest? Which produced the best quality? 
                How did the framework help Group 3?
              </p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}